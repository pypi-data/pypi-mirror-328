'use client'

import React, { memo, useMemo } from 'react'
import { Table, Button, Spinner } from '@radix-ui/themes'
import { encodeDataKey, FlowDataKey, FlowDataValue } from "@/lib/data/data";
import classNames from 'classnames';
import { useFlowContext } from '../flowContext';
import { useShallow } from 'zustand/shallow';
import { PartitionedTableRow, useTableRowData, useTableRows } from '../dataRequests/partitionedTable';
import { StructTypeAccessor, StructValueAccessor, ValueAccessor } from '@/lib/data/accessor';
import { ValueType } from '@/lib/data/schema';
import { DataValueView } from './DataValueView';
import { FieldName } from '@/lib/spec/flow';
import { create, StoreApi, UseBoundStore } from 'zustand';
import { PreviewContent } from './PreviewContent';

interface TableSelectionState {
  encodedKey: string | undefined;
  fieldName: FieldName | undefined;
  rowAccessor: StructValueAccessor | undefined;
  select: (encodedKey?: string, fieldName?: FieldName, rowAccessor?: StructValueAccessor) => void;
}

const showValueInCell = (type: ValueType, value: FlowDataValue) =>
  value == null ||
  typeof value === "boolean" ||
  typeof value === "number" ||
  (typeof value === "string" && value.length < 200) ||
  type.kind === "Range";

const DataTableCell = ({ type, value, onViewCellClick }: { type: ValueType, value: ValueAccessor | undefined, onViewCellClick?: () => void }) => {
  if (showValueInCell(type, value?.value)) {
    return <DataValueView type={type} value={value?.value} />;
  }
  return (
    <Button
      variant="soft"
      size="1"
      disabled={!onViewCellClick}
      onClick={onViewCellClick ? (e) => {
        e.stopPropagation();
        onViewCellClick();
      } : undefined}
    >
      View
    </Button>
  );
};

const DataTableRow = memo(function DataTableRow({ encodedKey, row, schema, useTableSelectionState }: {
  encodedKey: string, row: PartitionedTableRow, schema: StructTypeAccessor, useTableSelectionState: UseBoundStore<StoreApi<TableSelectionState>>
}) {
  const rowData = useTableRowData(row);
  const [select, selectedFieldName] = useTableSelectionState(useShallow(state =>
    [
      state.select,
      state.encodedKey === encodedKey ? state.fieldName : undefined
    ]
  ));
  return (
    <Table.Row
      className={classNames({ 'bg-[--iris-a2]': !!selectedFieldName })}
    >
      {schema.schema.fields.map((field, idx) => {
        const fieldValue = rowData ? rowData.fieldByName(field.name) : (idx === 0 ? row.key : undefined);
        return (<Table.Cell key={field.name}>
          {
            (!rowData && !fieldValue) ?
              <Spinner />
              :
              <DataTableCell
                type={field.type} value={fieldValue}
                onViewCellClick={() => rowData ? select(encodedKey, field.name, rowData) : undefined} />
          }
        </Table.Cell>)
      })}
    </Table.Row>
  );
});

const PreviewContentWrapper = ({ useTableSelectionState }: { useTableSelectionState: UseBoundStore<StoreApi<TableSelectionState>> }) => {
  const [rowAccessor, selectedFieldName] = useTableSelectionState(useShallow(state => [state.rowAccessor, state.fieldName]));
  if (rowAccessor && selectedFieldName) {
    const valueAccessor = rowAccessor.fieldByName(selectedFieldName);
    if (valueAccessor) {
      return <PreviewContent valueAccessor={valueAccessor} parentAccessor={rowAccessor} />;
    }
  }
};

export const DataTable = function () {
  const [topLevelFieldName, schema, tableRequest, setSelectedRow] = useFlowContext(useShallow(
    state => [
      state.topLevelFieldName,
      state.schema,
      state.topLevelFieldName ? state.getTableRequest(state.topLevelFieldName) : undefined,
      state.setSelectedRow
    ]));
  const rowSchema = topLevelFieldName && tableRequest ? schema.fieldByName(topLevelFieldName)?.type?.asCollection()?.element() : undefined;
  const rows = useTableRows(tableRequest);
  const useTableSelectionState = useMemo(() => create<TableSelectionState>((set) => {
    return {
      encodedKey: undefined,
      fieldName: undefined,
      rowAccessor: undefined,
      select: (encodedKey?: string, fieldName?: FieldName, rowAccessor?: StructValueAccessor) => {
        set({ encodedKey, fieldName, rowAccessor });
        setSelectedRow(rowAccessor);
      },
    };
  }), [setSelectedRow]);

  if (!rowSchema) return;
  if (!rows) return <Spinner />;
  return (
    <div className="p-4 flex flex-col">
      <div className='py-1'>
        <Table.Root>
          <Table.Header>
            <Table.Row>
              {rowSchema.schema.fields.map(field => (
                <Table.ColumnHeaderCell key={field.name}>
                  {field.name}
                </Table.ColumnHeaderCell>
              ))}
            </Table.Row>
          </Table.Header>

          <Table.Body>
            {rows.map(row => {
              const encodedKey = encodeDataKey(row.key.value as FlowDataKey);
              return (
                <DataTableRow key={encodedKey} encodedKey={encodedKey} row={row} schema={rowSchema} useTableSelectionState={useTableSelectionState} />
              )
            })}
          </Table.Body>
        </Table.Root>
      </div>
      <PreviewContentWrapper useTableSelectionState={useTableSelectionState} />
    </div>
  );
};