import { useMemo } from "react";
import * as druid from "@saehrimnir/druidjs";
import * as d3 from "d3";
import { useDataRequestsState } from "../dataRequests/dataRequestBase";
import { useShallow } from "zustand/shallow";
import { useFlowContext } from "../flowContext";
import { FlowInstanceQueryResponse } from "@/app/api/apiTypes";
import { findAccessPath, visitValues } from "@/lib/data/accessor";
import { VECTOR_ORIGIN_TEXT } from "@/lib/spec/fieldAttrs";

const getVectorFieldIdx = (resp: FlowInstanceQueryResponse): number => {
    const fieldIdx = resp.results.fields.findIndex(field => field.name === resp.info.vector_field_name);
    if (fieldIdx < 0) throw new Error('vector_field_name `' + resp.info.vector_field_name + '` not found in query response');
    return fieldIdx;
};

export const EmbeddingPlot = (): JSX.Element | undefined => {
    const selectedRow = useFlowContext(state => state.selectedRow);
    const searchRequests = useFlowContext(useShallow(state => state.searchSessions.map(session => session.request)));
    const searchStates = useDataRequestsState(searchRequests);

    const [queryEmbeddings, searchResultEmbeddings, dataEmbeddings] = useMemo(() => {
        const validSearchResponses = searchStates.map(state => state.response).filter(resp => !!resp);
        if (validSearchResponses.length === 0) return [undefined, undefined, undefined];

        const queryVectors: number[][] = validSearchResponses.map(response => response.info.query_vector);
        if (queryVectors.length < 2) {
            const results = validSearchResponses[0].results.results;
            queryVectors.push(results[results.length - 1].data[getVectorFieldIdx(validSearchResponses[0])] as number[]);
        }
        queryVectors.push(Array(queryVectors[0].length).fill(0));

        const dr = new druid.PCA(queryVectors);

        const searchResultEmbeddings: number[][] = [];
        for (const resp of validSearchResponses) {
            const vectorFieldIdx = getVectorFieldIdx(resp);
            searchResultEmbeddings.push(...resp.results.results.map(result => result.data[vectorFieldIdx] as number[]));
        }

        const dataEmbeddings: number[][] = [];
        if (selectedRow) {
            // TODO: Do we also want to filter by embedding model?
            const chunkFieldPaths = findAccessPath(selectedRow.structType.schema, field => !!field.attrs && (VECTOR_ORIGIN_TEXT in field.attrs));
            console.log(chunkFieldPaths);
            for (const path of chunkFieldPaths) {
                visitValues(selectedRow, path, accessor => {
                    const embeddingValue = accessor.value as number[];
                    if (embeddingValue) {
                        dataEmbeddings.push(embeddingValue);
                    }
                })
            }
        }
        return [
            dr.transform(queryVectors.slice(0, validSearchResponses.length)) as [number, number][],
            searchResultEmbeddings.length > 0 ? dr.transform(searchResultEmbeddings) as [number, number][] : [],
            dataEmbeddings.length > 0 ? dr.transform(dataEmbeddings) as [number, number][] : [],
        ];
    }, [selectedRow, searchStates]);

    const width = 800;
    const height = 800;
    const marginX = 20;
    const marginY = 20;

    const tx = d3.scaleLinear([-1, 1], [marginX, width - marginX]);
    const ty = d3.scaleLinear([1, -1], [marginY, height - marginY]);

    if (!queryEmbeddings) return;

    return <svg width={width} height={height}>
        <defs>
            <marker
                id="arrow"
                viewBox="0 0 10 10"
                refX="5"
                refY="5"
                markerWidth="6"
                markerHeight="6"
                orient="auto-start-reverse"
                fill="var(--yellow-a8)">
                <path d="M 0 0 L 10 5 L 0 10 z" />
            </marker>
        </defs>

        {dataEmbeddings.map(([x, y], i) =>
            <circle key={`data-${i}`} cx={tx(x)} cy={ty(y)} r={3} fill="var(--accent-a9)" />
        )}
        {searchResultEmbeddings.map(([x, y], i) =>
            <circle key={`search-${i}`} cx={tx(x)} cy={ty(y)} r={3} fill="none" stroke="var(--yellow-a8)" strokeWidth={1} />
        )}
        {queryEmbeddings.map(([x, y], i) =>
            <g key={`query-${i}`}>
                <line x1={tx(0)} y1={ty(0)} x2={tx(x)} y2={ty(y)} stroke="var(--yellow-a8)" strokeWidth={2} markerEnd="url(#arrow)" />
                <text x={tx(x * 1.05) - 20} y={ty(y * 1.05)} fontSize={12} fill="var(--yellow-a8)">Query {i + 1}</text>
            </g>
        )}
    </svg>;
};