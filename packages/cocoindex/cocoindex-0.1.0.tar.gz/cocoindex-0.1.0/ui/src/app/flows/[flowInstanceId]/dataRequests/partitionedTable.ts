import { FieldName } from "@/lib/spec/flow";
import { DocKeysRequest } from "./docKeys"
import { FlowInstanceDataRequest } from "./flowData";
import { DataRequestBase, useDataRequestState } from "./dataRequestBase";
import { StructValueAccessor, ValueAccessor, ValueTypeAccessor } from "@/lib/data/accessor";
import { FlowDataKey } from "@/lib/data/data";

export type PartitionedTableRow = {
    tableParam: PartitionedTableParams;
    key: ValueAccessor;
    rowRequest?: FlowInstanceDataRequest;
};

export type PartitionedTable = {
    rows: PartitionedTableRow[];
};

export type PartitionedTableParams = {
    flowInstName: string;
    field: FieldName;
};

export class PartitionedTableRequest extends DataRequestBase<PartitionedTableParams, PartitionedTable> {
    async request(param: PartitionedTableParams): Promise<PartitionedTable> {
        const docKeyResponse = await new DocKeysRequest({
            flowInstName: param.flowInstName,
            field: param.field,
        }).response();
        const keyTypeAccessor = new ValueTypeAccessor(docKeyResponse.key_type.type);
        const rows = docKeyResponse.keys.map(key => ({
            tableParam: param,
            key: new ValueAccessor(keyTypeAccessor, key),
        }));
        return { rows };
    }
}

export const useTableRows = (table: PartitionedTableRequest | undefined): PartitionedTableRow[] | undefined => {
    const tableState = useDataRequestState(table);
    return tableState?.response?.rows;
}

export const useTableRowData = (row: PartitionedTableRow | undefined): StructValueAccessor | undefined => {
    let rowRequest = row?.rowRequest;
    if (row && !rowRequest) {
        row.rowRequest = rowRequest = new FlowInstanceDataRequest({
            flowInstName: row.tableParam.flowInstName,
            field: row.tableParam.field,
            key: row.key.value as FlowDataKey,
        });
    }
    const rowRequestState = useDataRequestState(rowRequest);
    return row ? rowRequestState?.response?.fieldByName(row.tableParam.field)?.asCollection()?.rows()?.[0] : undefined;
}
