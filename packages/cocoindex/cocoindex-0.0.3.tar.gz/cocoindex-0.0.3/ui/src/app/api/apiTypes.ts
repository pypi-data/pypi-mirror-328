import { FlowDataKey, FlowDataValue } from "@/lib/data/data";
import { DataSchema, EnrichedValueType, FieldSchema } from "@/lib/data/schema";
import { SimilarityMetric } from "@/lib/math/embedding/similarity";
import { FieldName } from "@/lib/spec/flow";

export interface FlowInstanceKeysResponse {
    key_type: EnrichedValueType;
    keys: FlowDataKey[];
};

export interface FlowInstanceDataResponse {
    schema: DataSchema;
    data: FlowDataValue[] | null;
};


export interface FlowInstanceQueryResult {
    data: FlowDataValue[],
    score: number,
}

export interface FlowInstanceQueryResults {
    fields: FieldSchema[],
    results: FlowInstanceQueryResult[],
};

export interface SimpleSemanticsQueryInfo {
    similarity_metric: SimilarityMetric,
    query_vector: number[],
    vector_field_name: FieldName,
}

export interface FlowInstanceQueryResponse {
    results: FlowInstanceQueryResults,
    info: SimpleSemanticsQueryInfo,
};