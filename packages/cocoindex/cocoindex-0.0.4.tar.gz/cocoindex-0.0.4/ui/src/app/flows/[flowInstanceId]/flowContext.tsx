'use client'

import { createContext, useContext, useMemo } from "react";
import { create, UseBoundStore } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";
import { useParams } from "next/navigation";
import { FieldName } from "@/lib/spec/flow";
import { DocKeysRequest } from './dataRequests/docKeys';
import { SearchSession } from './dataRequests/search';
import { StoreApi } from 'zustand';
import { FlowInstanceSchemaRequest } from "./dataRequests/flowSchema";
import { useDataRequestState } from "./dataRequests/dataRequestBase";
import { PartitionedTableRequest } from "./dataRequests/partitionedTable";
import { StructTypeAccessor, StructValueAccessor } from "@/lib/data/accessor";

interface FlowState {
    schema: StructTypeAccessor;
    topLevelFieldName?: FieldName;
    activeTab: 'preview' | SearchSession;
    selectedRow?: StructValueAccessor;

    searchSessions: SearchSession[];
    setActiveTab: (activeTab: 'preview' | SearchSession) => void;
    setSelectedRow: (selectedRow?: StructValueAccessor) => void;
    setSearchSessions: (searchSessions: SearchSession[]) => void;
    getTableRequest: (fieldName: FieldName) => PartitionedTableRequest;
}

const FlowContext = createContext<UseBoundStore<StoreApi<FlowState>> | null>(null);

export const FlowContextProvider = ({ children }: { children: React.ReactNode }) => {
    const params = useParams();
    const flowInstanceId = params.flowInstanceId as string;
    const schemaRequest = useMemo(() => new FlowInstanceSchemaRequest({ flowInstName: flowInstanceId }), [flowInstanceId]);
    const schema = useDataRequestState(schemaRequest)?.response;

    // TODO: Select top-level field name if there're multiple.
    const topLevelFieldName = schema?.schema.fields[0]?.name;

    const useStore = useMemo(() => {
        const tableRequests = new Map<FieldName, PartitionedTableRequest>();
        return schema && create<FlowState>()(subscribeWithSelector((set) => {
            const initialState = {
                schema: new StructTypeAccessor(schema.schema),
                tableRequests: new Map(),
                topLevelFieldName,
                activeTab: 'preview' as const,
                docKeysRequest:
                    (!!topLevelFieldName ? new DocKeysRequest({
                        flowInstName: flowInstanceId,
                        field: topLevelFieldName,
                    }) : undefined),
                searchSessions: [],
            };

            return {
                ...initialState,
                setActiveTab: (activeTab: 'preview' | SearchSession) => {
                    set({ activeTab });
                },
                setSelectedRow: (selectedRow?: StructValueAccessor) => {
                    set({ selectedRow });
                },
                setSearchSessions: (searchSessions: SearchSession[]) => {
                    set({ searchSessions });
                },
                getTableRequest: (fieldName: FieldName) => {
                    let tableRequest = tableRequests.get(fieldName);
                    if (!tableRequest) {
                        tableRequest = new PartitionedTableRequest({ flowInstName: flowInstanceId, field: fieldName });
                        tableRequests.set(fieldName, tableRequest);
                    }
                    return tableRequest;
                },
            };
        }));
    }, [flowInstanceId, schema, topLevelFieldName]);

    if (!useStore) {
        return "Loading...";
    }
    return (
        <FlowContext.Provider value={useStore}>
            {children}
        </FlowContext.Provider>
    );
};

export const useFlowContext = <T,>(selector: (state: FlowState) => T): T => {
    const useStore = useContext(FlowContext);
    if (!useStore) {
        throw new Error('useFlowContext must be used within FlowContextProvider');
    }
    return useStore(selector);
};

export const useFlowContextStore = () => {
    const context = useContext(FlowContext);
    if (!context) {
        throw new Error('useFlowContextStore must be used within FlowContextProvider');
    }
    return context;
};
