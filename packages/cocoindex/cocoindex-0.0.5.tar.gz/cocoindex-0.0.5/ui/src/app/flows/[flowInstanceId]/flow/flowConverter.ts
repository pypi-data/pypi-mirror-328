import { FlowInstanceSpec, NamedSpec, ReactiveOpSpec } from '@/lib/spec/flow';
import { Node, Edge, Position } from 'reactflow';

// Global node size constants
const NODE_WIDTH = 300;
const NODE_HEIGHT = 600;
const NODE_SPACING = 150;

interface GraphNode {
  id: string;
  type: 'source' | 'sink' | 'op' | 'group' | 'grouproot';
  data?: unknown;
  parentId?: string;
  children?: GraphNode[];
  inputs?: ({ sourceId: string; fieldPath: string[] } | undefined)[];
  outputField?: string;
}

interface Graph {
  nodes: GraphNode[];
  edges: { source: string; target: string; sourceHandle: string; targetHandle: string; }[];
}

function convertFlowSpecToGraph(flowSpec: FlowInstanceSpec): Graph {
  const graph: Graph = { nodes: [], edges: [] };

  // Maps to track node output fields at each level
  const outputFieldNodeIdMaps: Map<string, string>[] = [new Map()];

  // Convert source nodes
  flowSpec.source_ops?.forEach((sourceOp) => {
    const node: GraphNode = {
      id: sourceOp.name,
      type: 'source',
      data: sourceOp,
      outputField: sourceOp.name
    };
    graph.nodes.push(node);
    outputFieldNodeIdMaps[0].set(sourceOp.name, sourceOp.kind);
  });

  function processReactiveOps(
    ops: NamedSpec<ReactiveOpSpec>[],
    parentId?: string,
    level: number = 0
  ): GraphNode[] {
    if (!outputFieldNodeIdMaps[level]) {
      outputFieldNodeIdMaps[level] = new Map();
    }

    const nodes: GraphNode[] = [];

    ops.forEach((op, index) => {
      if (op.action === 'ForEach') {
        const groupId = `ForEach ${index + 1}`;
        const groupNode: GraphNode = {
          id: groupId,
          type: 'group',
          data: { label: `ForEach ${index + 1}` },
          parentId,
          children: [],
          outputField: `${groupId}_output` // Added outputField for group node
        };

        // Add group root node, for connection
        const rootId = `${groupId}_root`;
        const rootNode: GraphNode = {
          id: rootId,
          type: 'grouproot',
          //   data: op,
          parentId: groupId,
          outputField: `${groupId}_output`,
          inputs: op.field_path ? [{ sourceId: '', fieldPath: op.field_path }] : []
        };
        groupNode.children!.push(rootNode);

        // Create edges for root node inputs
        if (rootNode.inputs) {
          rootNode.inputs.forEach(input => {
            if (!input?.fieldPath) return;

            let sourceNodeId;
            let currentLevel = 0;

            while (currentLevel in outputFieldNodeIdMaps) {
              sourceNodeId = outputFieldNodeIdMaps[currentLevel]?.get(input.fieldPath[0]);
              if (sourceNodeId) break;
              currentLevel++;
            }

            if (sourceNodeId) {
              graph.edges.push({
                source: sourceNodeId,
                target: rootId,
                sourceHandle: input.fieldPath[0],
                targetHandle: rootId
              });
            }
          });
        }

        // Process nested ops
        if (op.op_scope.ops) {
          const nestedNodes = processReactiveOps(op.op_scope.ops, groupId, level + 1);
          groupNode.children!.push(...nestedNodes);
        }

        nodes.push(groupNode);

      } else if (op.action === 'Collect') {
        const node: GraphNode = {
          id: op.name,
          type: 'sink',
          data: op,
          parentId,
          inputs: [{
            sourceId: '',
            fieldPath: op.input.field_path,
          }],
        };
        nodes.push(node);

        // Create edges for collect inputs
        if (node.inputs) {
          node.inputs.forEach(input => {
            if (!input?.fieldPath) return;

            let sourceNodeId;
            let currentLevel = 0;

            while (currentLevel in outputFieldNodeIdMaps) {
              sourceNodeId = outputFieldNodeIdMaps[currentLevel]?.get(input.fieldPath[0]);
              if (sourceNodeId) break;
              currentLevel++;
            }

            if (sourceNodeId) {
              graph.edges.push({
                source: sourceNodeId,
                target: node.id,
                sourceHandle: input.fieldPath[0],
                targetHandle: node.id
              });
            }
          });
        }
      } else if (op.action === 'Transform') {
        // Regular operation node
        const nodeId = op.name;
        const node: GraphNode = {
          id: nodeId,
          type: 'op',
          data: op,
          parentId,
          outputField: op.name,
          inputs: op.inputs?.map(input => (input.kind === 'Field' ? {
            sourceId: '',
            fieldPath: input.field_path,
          } : undefined)),
        };
        nodes.push(node);

        // Track output field
        if (node.outputField) {
          outputFieldNodeIdMaps[level].set(node.outputField, nodeId);
        }

        // Create edges for inputs
        if (node.inputs) {
          node.inputs.forEach(input => {
            if (!input) return;

            let sourceNodeId;
            let currentLevel = 0;

            while (currentLevel in outputFieldNodeIdMaps) {
              sourceNodeId = outputFieldNodeIdMaps[currentLevel]?.get(input.fieldPath[0]);
              if (sourceNodeId) break;
              currentLevel++;
            }

            if (sourceNodeId) {
              graph.edges.push({
                source: sourceNodeId,
                target: nodeId,
                sourceHandle: input.fieldPath[0],
                targetHandle: nodeId
              });
            }
          });
        }
      } else {
        console.error("Unknown operation", op);
      }
    });

    return nodes;
  }

  if (flowSpec.reactive_ops) {
    graph.nodes.push(...processReactiveOps(flowSpec.reactive_ops));
  }

  return graph;
}

export function convertFlowSpecToReactFlow(flowSpec: FlowInstanceSpec) {
  const graph = convertFlowSpecToGraph(flowSpec);
  const nodes: Node[] = [];
  const edges: Edge[] = [];

  function layoutNodes(graphNodes: GraphNode[], level: number = 0, parentId?: string) {
    let nodeIndex = 0;

    graphNodes.forEach(graphNode => {
      const xPos = nodeIndex * (NODE_WIDTH + NODE_SPACING);

      if (graphNode.type === 'group') {
        // Calculate group dimensions
        const childCount = (graphNode.children?.length || 0) + 1;
        const groupWidth = childCount * (NODE_WIDTH + NODE_SPACING);
        const groupHeight = NODE_HEIGHT + 100;

        nodes.push({
          id: graphNode.id,
          type: 'group',
          data: graphNode.data,
          position: { x: xPos, y: 0 },
          parentNode: parentId,
          style: {
            width: groupWidth,
            height: groupHeight,
            backgroundColor: 'transparent'
          }
        });

        if (graphNode.children) {
          layoutNodes(graphNode.children, level + 1, graphNode.id);
        }

        nodeIndex++;

      } else if (graphNode.type === 'grouproot') {
        const parentNode = nodes.find(n => n.id === parentId);
        const parentHeight = (parentNode?.style?.height as number) || NODE_HEIGHT;

        nodes.push({
          id: graphNode.id,
          type: graphNode.type,
          data: graphNode.data,
          position: { x: xPos, y: (parentHeight - NODE_HEIGHT) / 2 },
          parentNode: parentId,
          sourcePosition: Position.Right,
          targetPosition: Position.Left,
          width: NODE_WIDTH,
          height: NODE_HEIGHT
        });
      } else {
        const parentNode = nodes.find(n => n.id === parentId);
        const parentHeight = (parentNode?.style?.height as number) || NODE_HEIGHT;

        nodes.push({
          id: graphNode.id,
          type: graphNode.type,
          data: graphNode.data,
          position: { x: xPos, y: (parentHeight - NODE_HEIGHT) / 2 },
          parentNode: parentId,
          sourcePosition: Position.Right,
          targetPosition: Position.Left,
          width: NODE_WIDTH,
          height: NODE_HEIGHT
        });

        nodeIndex++;
      }
    });
  }

  layoutNodes(graph.nodes);

  // Convert graph edges to ReactFlow edges
  graph.edges.forEach(edge => {
    edges.push({
      id: `${edge.source}_${edge.target}`,
      ...edge
    });
  });

  return { nodes, edges };
}