// Type definitions mirroring src/base/spec.rs

import { SimilarityMetric } from "../math/embedding/similarity";

export type ScopeName = string;
export type FieldName = string;

export type FieldPath = FieldName[];

export type OpArgName = string | null | undefined;

export type NamedSpec<T> = {
    name: string;
} & T;

export interface FieldMapping {
    scope?: ScopeName;
    field_path: FieldPath;
}

export interface LiteralMapping {
    value: unknown;
}

export interface StructMapping {
    fields: NamedSpec<ValueMapping>[];
}

export type ValueMapping
    = { kind: 'Literal' } & LiteralMapping
    | { kind: 'Field' } & FieldMapping
    | { kind: 'Struct' } & StructMapping;

export type OpArgBinding = {
    arg_name: OpArgName;
} & ValueMapping;

export interface OpSpec {
    kind: string;
    [key: string]: unknown;
}

export interface TransformOpSpec {
    action: 'Transform';
    inputs: OpArgBinding[];
    op: OpSpec;
}

export interface ForEachOpSpec {
    action: 'ForEach';
    field_path: FieldPath;
    op_scope: ReactiveOpScope;
}

export interface CollectOpSpec {
    action: 'Collect';
    input: FieldMapping;
    scope_name: ScopeName;
    collector_name: FieldName;
}

export interface VectorIndexDef {
    field_name: FieldName;
    metric: SimilarityMetric;
}

export interface IndexOptions {
    primary_key_fields?: FieldName[];
    vector_index_defs?: VectorIndexDef[];
}

export interface ExportOpSpec {
    collector_name: FieldName;
    target: OpSpec;
    index_options: IndexOptions;
}

export type ReactiveOpSpec
    = TransformOpSpec
    | ForEachOpSpec
    | CollectOpSpec
    ;

export interface ReactiveOpScope {
    name: ScopeName;
    ops: NamedSpec<ReactiveOpSpec>[];
}

export interface FlowInstanceSpec {
    name: string;
    source_ops?: NamedSpec<OpSpec>[];
    reactive_ops?: NamedSpec<ReactiveOpSpec>[];
    export_ops?: NamedSpec<ExportOpSpec>[];
}