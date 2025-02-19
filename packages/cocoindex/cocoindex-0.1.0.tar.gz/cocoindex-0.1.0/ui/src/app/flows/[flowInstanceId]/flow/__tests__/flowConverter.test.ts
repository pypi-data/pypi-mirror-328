import { convertFlowSpecToReactFlow } from '../flowConverter';
import { flowSpec } from './FilesEmbedding';

describe('Flow Converter', () => {
    it('should correctly convert flow spec to react flow format', () => {
        const result = convertFlowSpecToReactFlow(flowSpec);
        
        expect(result).toEqual({
            nodes: [
                {
                    id: 'LocalFile',
                    type: 'source',
                    data: {
                        name: 'documents',
                        kind: 'LocalFile',
                        path: 'devData/sourceFiles'
                    },
                    position: { x: 0, y: 0 },
                    sourcePosition: 'right'
                },
                {
                    id: 'ForEach 1',
                    type: 'group',
                    data: { label: 'ForEach 1' },
                    position: { x: 300, y: 0 },
                    style: {
                        width: 500,
                        height: 200,
                        backgroundColor: 'transparent'
                    }
                },
                {
                    id: 'ForEach 1_root',
                    type: 'op',
                    data: {
                        name: '.foreach.0',
                        action: 'ForEach',
                        field_path: ['documents'],
                        op_scope: {
                            name: '_documents_0',
                            ops: [
                                {
                                    action: 'Transform',
                                    inputs: [{
                                        kind: 'Field',
                                        scope: '_documents_0',
                                        field_path: ['content']
                                    }],
                                    name: 'markdown',
                                    op: {
                                        kind: 'ToMarkdown'
                                    }
                                },
                                {
                                    action: 'Transform',
                                    inputs: [{
                                        kind: 'Field',
                                        scope: '_documents_0',
                                        field_path: ['markdown']
                                    }],
                                    name: 'chunks',
                                    op: {
                                        kind: 'SplitRecursively',
                                        chunk_overlap: 100,
                                        chunk_size: 300,
                                        language: 'markdown'
                                    }
                                },
                                {
                                    action: 'ForEach',
                                    field_path: ['chunks'],
                                    name: '.foreach.1',
                                    op_scope: {
                                        name: '_chunks_1',
                                        ops: [
                                            {
                                                action: 'Transform',
                                                inputs: [{
                                                    kind: 'Field',
                                                    scope: '_chunks_1',
                                                    field_path: ['text']
                                                }],
                                                name: 'embedding',
                                                op: {
                                                    kind: 'SentenceTransformerEmbed',
                                                    model: 'sentence-transformers/all-MiniLM-L6-v2'
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    },
                    position: { x: 320, y: 25 },
                    parentNode: 'ForEach 1',
                    sourcePosition: 'right',
                    targetPosition: 'left',
                    width: 50,
                    height: 50
                },
                {
                    id: 'ToMarkdown',
                    type: 'op',
                    data: {
                        name: 'markdown',
                        action: 'Transform',
                        inputs: [{
                            kind: 'Field',
                            scope: '_documents_0',
                            field_path: ['content']
                        }],
                        op: {
                            kind: 'ToMarkdown'
                        }
                    },
                    position: { x: 350, y: 50 },
                    parentNode: 'ForEach 1',
                    sourcePosition: 'right',
                    targetPosition: 'left'
                },
                {
                    id: 'SplitRecursively',
                    type: 'op',
                    data: {
                        name: 'chunks',
                        action: 'Transform',
                        inputs: [{
                            kind: 'Field',
                            scope: '_documents_0',
                            field_path: ['markdown']
                        }],
                        op: {
                            kind: 'SplitRecursively',
                            chunk_overlap: 100,
                            chunk_size: 300,
                            language: 'markdown'
                        }
                    },
                    position: { x: 550, y: 50 },
                    parentNode: 'ForEach 1',
                    sourcePosition: 'right',
                    targetPosition: 'left'
                },
                {
                    id: 'ForEach 3',
                    type: 'group',
                    data: { label: 'ForEach 3' },
                    position: { x: 400, y: 100 },
                    parentNode: 'ForEach 1',
                    style: {
                        width: 500,
                        height: 200,
                        backgroundColor: 'transparent'
                    }
                },
                {
                    id: 'ForEach 3_root',
                    type: 'op',
                    data: {
                        name: '.foreach.1',
                        action: 'ForEach',
                        field_path: ['chunks'],
                        op_scope: {
                            name: '_chunks_1',
                            ops: [
                                {
                                    action: 'Transform',
                                    inputs: [{
                                        kind: 'Field',
                                        scope: '_chunks_1',
                                        field_path: ['text']
                                    }],
                                    name: 'embedding',
                                    op: {
                                        kind: 'SentenceTransformerEmbed',
                                        model: 'sentence-transformers/all-MiniLM-L6-v2'
                                    }
                                }
                            ]
                        }
                    },
                    position: { x: 320, y: 125 },
                    parentNode: 'ForEach 3',
                    sourcePosition: 'right',
                    targetPosition: 'left',
                    width: 50,
                    height: 50
                },
                {
                    id: 'SentenceTransformerEmbed',
                    type: 'op',
                    data: {
                        name: 'embedding',
                        action: 'Transform',
                        inputs: [{
                            kind: 'Field',
                            scope: '_chunks_1',
                            field_path: ['text']
                        }],
                        op: {
                            kind: 'SentenceTransformerEmbed',
                            model: 'sentence-transformers/all-MiniLM-L6-v2'
                        }
                    },
                    position: { x: 350, y: 50 },
                    parentNode: 'ForEach 3',
                    sourcePosition: 'right',
                    targetPosition: 'left'
                }
            ],
            edges: [
                {
                    id: 'LocalFile_ForEach 1_root',
                    source: 'LocalFile',
                    target: 'ForEach 1_root',
                    sourceHandle: 'documents',
                    targetHandle: 'ForEach 1_root'
                },
                {
                    id: 'ForEach 1_root_ToMarkdown',
                    source: 'ForEach 1_root',
                    sourceHandle: 'content',
                    target: 'ToMarkdown',
                    targetHandle: 'markdown'
                },
                {
                    id: 'ToMarkdown_SplitRecursively',
                    source: 'ToMarkdown',
                    target: 'SplitRecursively',
                    sourceHandle: 'markdown',
                    targetHandle: 'chunks'
                },
                {
                    id: 'SplitRecursively_ForEach 3_root',
                    source: 'SplitRecursively',
                    target: 'ForEach 3_root',
                    sourceHandle: 'chunks',
                    targetHandle: 'ForEach 3_root'
                },
                {
                    id: 'ForEach 3_root_SentenceTransformerEmbed',
                    source: 'ForEach 3_root',
                    sourceHandle: 'text',
                    target: 'SentenceTransformerEmbed',
                    targetHandle: 'embedding'
                }
            ]
        });
    });
});