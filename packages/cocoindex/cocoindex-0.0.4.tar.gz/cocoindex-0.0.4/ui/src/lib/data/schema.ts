import { FlowDataValue } from "./data";

// Basic value types matching Rust's BasicValueType enum
export type VectorTypeSchema = {
    element_type: BasicValueType;
    dimension?: number;
};

export type BasicValueType =
    | { kind: 'Bytes' }
    | { kind: 'Str' }
    | { kind: 'Bool' }
    | { kind: 'Int64' }
    | { kind: 'Float32' }
    | { kind: 'Float64' }
    | { kind: 'Range' }
    | { kind: 'Json' }
    | { kind: 'Vector'; element_type: BasicValueType; dimension?: number };

// Field schema types
export type FieldSchema = {
    name: string;
} & EnrichedValueType;

// Struct schema
export type StructSchema = {
    fields: FieldSchema[];
};

export type StructType = {
    kind: 'Struct';
} & StructSchema;

// Collection related types
export type CollectionKind = 'Collection' | 'Table' | 'List';

export type CollectionType = {
    kind: CollectionKind;
    element: StructSchema;
    collectors?: Array<{
        name: string;
        spec: StructSchema;
    }>;
};

// Value type that can be either basic, struct, or collection
export type ValueType =
    | BasicValueType
    | StructType
    | CollectionType
    ;

export const isStructType = (type: ValueType): type is StructType => {
    return type.kind === 'Struct';
}

export const isCollectionType = (type: ValueType): type is CollectionType => {
    return type.kind === 'Collection' || type.kind === 'Table' || type.kind === 'List';
}

export const isBasicValueType = (type: ValueType): type is BasicValueType => {
    return !isStructType(type) && !isCollectionType(type);
}

export type EnrichedValueType = {
    type: ValueType;
    nullable?: boolean;
    attrs?: Record<string, unknown>;
};

// Main DataSchema type
export type DataSchema = {
    schema: StructSchema;
    collectors?: Array<{
        name: string;
        spec: StructSchema;
    }>;
};

export type AnalyzedLocalFieldReference = {
    fields_idx: number[];
}

export type AnalyzedFieldReference = {
    local: AnalyzedLocalFieldReference;
    scope_up_level?: number;
}

export type AnalyzedStructMapping = {
    fields: AnalyzedValueMapping[];
}

export type AnalyzedValueMapping =
    | { kind: 'Literal'; value: FlowDataValue }
    | { kind: 'Field' } & AnalyzedFieldReference
    | { kind: 'Struct' } & AnalyzedStructMapping;
