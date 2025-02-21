import { FieldName } from "../spec/flow";
import { FlowDataValue } from "./data";
import { CollectionType, FieldSchema, isCollectionType, isStructType, StructSchema, ValueType } from "./schema";


export type FieldSchemaAccessor = {
    type: ValueTypeAccessor;
    attrs?: Record<string, unknown>;
};
export class ValueTypeAccessor {
    type: ValueType;

    constructor(type: ValueType) {
        this.type = type;
    }

    asStruct(): StructTypeAccessor | undefined {
        if (isStructType(this.type)) {
            return new StructTypeAccessor(this.type)
        }
    }

    asCollection(): CollectionTypeAccessor | undefined {
        if (isCollectionType(this.type)) {
            return new CollectionTypeAccessor(this.type);
        }
    }
}

export class StructTypeAccessor {
    schema: StructSchema;

    constructor(schema: StructSchema) {
        this.schema = schema;
    }

    findFieldIndex(name: FieldName): number | undefined {
        // TODO: Create a map in the constructor to make this faster.
        const index = this.schema.fields.findIndex(field => field.name === name);
        if (index >= 0) {
            return index;
        }
        return undefined;
    }

    fieldTypeById(id: number): ValueTypeAccessor {
        return new ValueTypeAccessor(this.schema.fields[id].type);
    }

    fieldById(id: number): FieldSchemaAccessor {
        const field = this.schema.fields[id];
        return {
            type: new ValueTypeAccessor(field.type),
            attrs: field.attrs,
        };
    }

    fieldByName(name: FieldName): FieldSchemaAccessor | undefined {
        const fieldId = this.findFieldIndex(name);
        return fieldId != null ? this.fieldById(fieldId) : undefined;
    }

    fields(): FieldSchemaAccessor[] {
        return this.schema.fields.map((_, idx) => this.fieldById(idx));
    }
}

export class CollectionTypeAccessor {
    type: CollectionType;

    constructor(type: CollectionType) {
        this.type = type;
    }

    element(): StructTypeAccessor {
        return new StructTypeAccessor(this.type.element);
    }
}

export class ValueAccessor {
    type: ValueTypeAccessor;
    value: FlowDataValue;

    constructor(type: ValueTypeAccessor, value: FlowDataValue) {
        this.type = type;
        this.value = value;
    }

    asStruct(): StructValueAccessor | undefined {
        const structType = this.type.asStruct();
        return structType && new StructValueAccessor(structType, this.value as (FlowDataValue[] | null));
    }

    asCollection(): CollectionValueAccessor | undefined {
        const collectionType = this.type.asCollection()
        return collectionType && new CollectionValueAccessor(collectionType, this.value as (FlowDataValue[][] | null));
    }
}

export class FieldAccessor extends ValueAccessor {
    schema: FieldSchemaAccessor;

    constructor(schema: FieldSchemaAccessor, value: FlowDataValue) {
        super(new ValueTypeAccessor(schema.type.type), value);
        this.schema = schema;
    }
}

export class StructValueAccessor {
    structType: StructTypeAccessor;
    fieldValues: FlowDataValue[] | null;

    constructor(structType: StructTypeAccessor, fieldValues: FlowDataValue[] | null) {
        this.structType = structType;
        this.fieldValues = fieldValues;
    }

    fieldById(id: number): FieldAccessor | undefined {
        if (this.fieldValues == null) return undefined;
        return new FieldAccessor(this.structType.fieldById(id), this.fieldValues[id]);
    }

    fieldByIds(ids: number[]): FieldAccessor | undefined {
        if (ids.length === 0) return undefined;
        let type = this.structType;
        let values = this.fieldValues;

        for (let i = 0; i < ids.length; ++i) {
            const fieldId = ids[i];
            const fieldSchema = type.fieldById(fieldId);
            const fieldValue = values?.[fieldId];
            if (!fieldSchema) {
                return undefined;
            }
            if (i === ids.length - 1) {
                return new FieldAccessor(fieldSchema, fieldValue);
            }

            const structType = fieldSchema.type.asStruct();
            if (!structType) {
                return undefined;
            }
            type = structType;
            values = fieldValue as FlowDataValue[];
        }
    }

    fieldByName(name: FieldName): FieldAccessor | undefined {
        const fieldId = this.structType.findFieldIndex(name);
        return fieldId !== undefined ? this.fieldById(fieldId) : undefined;
    }

    fields(): ValueAccessor[] {
        return this.fieldValues?.map((v, i) => new ValueAccessor(this.structType.fieldTypeById(i), v)) ?? [];
    }
}

export class CollectionValueAccessor {
    collectionType: CollectionTypeAccessor;
    elementValues: FlowDataValue[][] | null;

    constructor(collectionType: CollectionTypeAccessor, elementValues: FlowDataValue[][] | null) {
        this.collectionType = collectionType;
        this.elementValues = elementValues;
    }

    rows(): StructValueAccessor[] | undefined {
        if (this.elementValues == null) return undefined;
        const elementType = this.collectionType.element();
        return this.elementValues.map(v => new StructValueAccessor(elementType, v));
    }
}

export type AccessStep = { fieldIdx: number } | 'eachRow';
export type AccessPath = AccessStep[];

export const findAccessPath = (structSchema: StructSchema, predicate: (accessor: FieldSchema) => boolean): AccessPath[] => {
    const result: AccessPath[] = [];

    const visitStruct = (structSchema: StructSchema, prevPath: AccessPath) => {
        structSchema.fields.forEach((field, i) => {
            prevPath.push({ fieldIdx: i });
            if (predicate(field)) {
                result.push([...prevPath]);
            }
            visit(field.type, prevPath);
            prevPath.pop();
        });
    };
    const visit = (type: ValueType, prevPath: AccessPath) => {
        if (isStructType(type)) {
            visitStruct(type, prevPath);
        } else if (isCollectionType(type)) {
            prevPath.push('eachRow');
            visitStruct(type.element, prevPath);
            prevPath.pop();
        }
    };
    visitStruct(structSchema, []);
    return result;
};

export const visitValues = (accessor: StructValueAccessor, path: AccessPath, visitor: (accessor: ValueAccessor) => void) => {
    const visitStruct = (accessor: StructValueAccessor, stepIdx: number) => {
        const step = path[stepIdx];
        const fieldIdx = step === 'eachRow' ? undefined : step.fieldIdx;
        const field = fieldIdx !== undefined ? accessor.fieldById(fieldIdx) : undefined;
        if (field) {
            visit(field, stepIdx + 1);
        } else {
            console.error("visitValues: field not found", path, stepIdx);
        }
    };
    const visit = (accessor: ValueAccessor, stepIdx: number) => {
        if (stepIdx >= path.length) {
            visitor(accessor);
            return;
        }
        const step = path[stepIdx];
        if (step === 'eachRow') {
            const collection = accessor.asCollection();
            if (collection) {
                const rows = collection.rows();
                if (rows) {
                    for (const row of rows) {
                        visitStruct(row, stepIdx + 1);
                    }
                }
            } else {
                console.error("visitValues: expect collection", path, stepIdx);
            }
        } else {
            const structAccessor = accessor.asStruct();
            if (structAccessor) {
                visitStruct(structAccessor, stepIdx);
            } else {
                console.error("visitValues: expect struct", path, stepIdx);
            }
        }
    };
    visitStruct(accessor, 0);
};


