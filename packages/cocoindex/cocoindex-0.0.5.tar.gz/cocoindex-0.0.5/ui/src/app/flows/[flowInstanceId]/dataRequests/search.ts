import { DataRequestBase } from "./dataRequestBase";
import { ErrorResponse } from "@/app/api/response";
import { SIMILARITY_METRICS, SimilarityMetric } from "@/lib/math/embedding/similarity";
import { FlowInstanceQueryResponse } from "@/app/api/apiTypes";
import { create, StoreApi, UseBoundStore } from "zustand";
import { API_URL } from "@/constants";

export type SearchParams = {
    flowInstName: string;
    query: string;
    limit: number;
    metric: SimilarityMetric;
};

export class SearchRequest extends DataRequestBase<SearchParams | undefined, FlowInstanceQueryResponse> {
    async request(param: SearchParams): Promise<FlowInstanceQueryResponse | ErrorResponse> {
        const encodedParams = [`query=${encodeURIComponent(param.query)}`, `limit=${param.limit}`];
        if (param.metric) {
            encodedParams.push(`metric=${param.metric}`);
        }
        return fetch(`${API_URL}/flows/${encodeURIComponent(param.flowInstName)}/search?${encodedParams.join('&')}`).then(res => res.json());
    }
}

type SearchParamsStore = {
    value: SearchParams;
    setValue: (value: SearchParams) => void;
};

export type SearchSession = {
    useDraftParams: UseBoundStore<StoreApi<SearchParamsStore>>;
    request: SearchRequest;
};

export const createSearchSession = (flowInstName: string): SearchSession => {
    return {
        useDraftParams: create((set) => ({
            value: { flowInstName, query: '', limit: 20, metric: SIMILARITY_METRICS[0] },
            setValue: (value: SearchParams) => {
                set({ value });
            },
        })),
        request: new SearchRequest(undefined),
    };
};
