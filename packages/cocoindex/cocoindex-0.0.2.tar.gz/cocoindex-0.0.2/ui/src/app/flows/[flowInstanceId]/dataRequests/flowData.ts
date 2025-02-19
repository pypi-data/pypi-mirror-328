import { ErrorResponse } from "@/app/api/response";
import { dataKeyToStrs, FlowDataKey } from "@/lib/data/data";
import { FieldName } from "@/lib/spec/flow";
import { DataRequestBase } from "./dataRequestBase";
import { API_URL } from "@/constants";
import { StructTypeAccessor, StructValueAccessor } from "@/lib/data/accessor";

export type FlowInstanceDataParams = {
    flowInstName: string;
    field: FieldName;
    key: FlowDataKey;
};

export class FlowInstanceDataRequest extends DataRequestBase<FlowInstanceDataParams, StructValueAccessor> {
    async request(param: FlowInstanceDataParams): Promise<StructValueAccessor | ErrorResponse> {
        const encodedParams = [`field=${encodeURIComponent(param.field)}`];
        if (param.key) {
            for (const key of dataKeyToStrs(param.key)) {
                encodedParams.push(`key=${encodeURIComponent(key)}`);
            }
        }
        const resp = await fetch(`${API_URL}/flows/${encodeURIComponent(param.flowInstName)}/data?${encodedParams.join('&')}`);
        const respJson = await resp.json();
        return new StructValueAccessor(new StructTypeAccessor(respJson.schema.schema), respJson.data);
    }
}