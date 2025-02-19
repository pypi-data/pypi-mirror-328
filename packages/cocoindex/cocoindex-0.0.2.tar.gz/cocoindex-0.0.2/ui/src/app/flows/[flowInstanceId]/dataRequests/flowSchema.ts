import { DataSchema } from "@/lib/data/schema";
import { DataRequestBase } from "./dataRequestBase";
import { ErrorResponse } from "@/app/api/response";
import { API_URL } from "@/constants";

export type FlowInstanceSchemaParams = {
    flowInstName: string;
};

export class FlowInstanceSchemaRequest extends DataRequestBase<FlowInstanceSchemaParams, DataSchema> {
    async request(param: FlowInstanceSchemaParams): Promise<DataSchema | ErrorResponse> {
        return fetch(`${API_URL}/flows/${encodeURIComponent(param.flowInstName)}/schema`).then(res => res.json());
    }
}
