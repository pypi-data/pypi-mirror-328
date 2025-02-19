'use client'

import { useCallback, useEffect, useState } from 'react'
import ReactFlow, {
    Background,
    useNodesState,
    useEdgesState,
    addEdge,
    Connection,
    Controls,
    MiniMap,
    NodeTypes
} from 'reactflow'
import 'reactflow/dist/style.css'
import "./flow.css";
import { convertFlowSpecToReactFlow } from './flowConverter';
import OpNode from './OpNode';
import SourceNode from './SourceNode';
import SinkNode from './SinkNode';
import StoreNode from './StoreNode';
import GroupRootNode from './GroupRootNode';
import { IconButton, Button, Spinner } from '@radix-ui/themes';
import { CiMap } from "react-icons/ci";
import { IoPlayOutline } from "react-icons/io5";
import { API_URL } from "@/constants";
import { FlowInstanceSpec } from '@/lib/spec/flow';

const nodeTypes: NodeTypes = {
    op: OpNode,
    source: SourceNode,
    sink: SinkNode,
    export: StoreNode,
    grouproot: GroupRootNode,
};

interface FlowProps {
    flowInstanceId: string;
}

export function Flow({ flowInstanceId }: FlowProps): JSX.Element {
    const [nodes, setNodes, onNodesChange] = useNodesState([]);
    const [edges, setEdges, onEdgesChange] = useEdgesState([]);
    const [showMiniMap, setShowMiniMap] = useState(false);
    const [isBuilding, setIsBuilding] = useState(false);

    useEffect(() => {
        async function fetchFlowSpec() {
            const response = await fetch(`${API_URL}/flows/${flowInstanceId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch flow spec');
            }
            const flowSpec: FlowInstanceSpec = await response.json();
            const { nodes, edges } = convertFlowSpecToReactFlow(flowSpec);
            setNodes(nodes);
            setEdges(edges);
        }
        fetchFlowSpec();
    }, [flowInstanceId, setNodes, setEdges]);

    const onConnect = useCallback(
        (params: Connection) =>
            setEdges((eds) =>
                addEdge({ ...params, animated: true }, eds),
            ),
        [setEdges],
    );

    const handleBuildIndex = async () => {
        setIsBuilding(true);
        try {
            const response = await fetch(`${API_URL}/flows/${flowInstanceId}/buildIndex`, {
                method: 'POST',
            });
            if (!response.ok) {
                throw new Error('Failed to build index');
            }
        } catch (error) {
            console.error('Error building index:', error);
        } finally {
            setIsBuilding(false);
        }
    };

    return (
        <div className='w-full h-full layer-1'>
            <div className="absolute top-2 right-4 z-10 flex gap-2">
                <Button variant="solid" size="1" radius="medium" onClick={handleBuildIndex} disabled={isBuilding}>
                    {isBuilding ? (
                        <>
                            <Spinner />
                            Building...
                        </>
                    ) : (
                        <>
                            <IoPlayOutline />
                            Build Index
                        </>
                    )}
                </Button>
            </div>
            <div className="absolute bottom-6 right-4 z-10">
                <IconButton
                    variant="soft"
                    onClick={() => setShowMiniMap(!showMiniMap)}
                    title={showMiniMap ? "Hide minimap" : "Show minimap"}
                >
                    <CiMap />
                </IconButton>
            </div>
            <ReactFlow
                nodes={nodes}
                nodeTypes={nodeTypes}
                edges={edges}
                onNodesChange={onNodesChange}
                onEdgesChange={onEdgesChange}
                onConnect={onConnect}
                fitView
                nodesDraggable={false}
                nodesConnectable={false}
            >
                <Background color="var(--gray-a4)" gap={40} size={4} />
                <Controls />
                {showMiniMap && <MiniMap pannable={true} className='opacity-80' />}
            </ReactFlow>
        </div>
    )
}