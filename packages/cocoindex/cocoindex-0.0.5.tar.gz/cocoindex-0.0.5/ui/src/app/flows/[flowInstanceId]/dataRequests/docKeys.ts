import { FieldName } from "@/lib/spec/flow";
import { ErrorResponse } from "@/app/api/response";
import { DataRequestBase } from "./dataRequestBase";
import { FlowInstanceKeysResponse } from "@/app/api/apiTypes";
import { API_URL } from "@/constants";

export type DocKeysParams = {
    flowInstName: string;
    field: FieldName;
};

export class DocKeysRequest extends DataRequestBase<DocKeysParams, FlowInstanceKeysResponse> {
    async request(param: DocKeysParams): Promise<FlowInstanceKeysResponse | ErrorResponse> {
        const encodedParams = `field=${encodeURIComponent(param.field)}`;
        return fetch(`${API_URL}/flows/${encodeURIComponent(param.flowInstName)}/keys?${encodedParams}`).then(res => res.json());
    }
}
