import { ErrorResponse, isErrorResponse } from "@/app/api/response";
import { useCallback, useRef, useSyncExternalStore } from "react";

export class DataRequestState<ParamType, ResponseType> {
    param: ParamType;
    response?: ResponseType;
    error?: Error;

    constructor(param: ParamType) {
        this.param = param;
    }

    collapsed(): DataRequestState<NonNullable<ParamType>, ResponseType> | undefined {
        if (this.param == undefined) return undefined;
        const result = new DataRequestState<NonNullable<ParamType>, ResponseType>(this.param);
        result.response = this.response;
        result.error = this.error;
        return result;
    }
}


export abstract class DataRequestBase<ParamType, ResponseType> {
    state: DataRequestState<ParamType, ResponseType>;
    abstract request(param: NonNullable<ParamType>): Promise<ResponseType | ErrorResponse>;

    private subscribers_: (() => void)[];

    constructor(param: ParamType) {
        this.subscribers_ = [];
        this.state = new DataRequestState(param);
        this.refreshResponse_();
    }

    setParam(param: ParamType): void {
        if (param !== this.state.param) {
            this.setState_(param);
            this.refreshResponse_();
        }
    }

    async response(): Promise<ResponseType> {
        if (!this.state.response && !this.state.error) {
            let unsubscribe: (() => void) | undefined;
            await new Promise((resolve) => {
                unsubscribe = this.subscribe(() => {
                    if (this.state.response) {
                        resolve(this.state.response);
                    }
                });
            });
            unsubscribe?.();
        }
        if (this.state.error) {
            throw this.state.error;
        }
        if (!this.state.response) {
            throw new Error("No response got");
        }
        return this.state.response;
    }

    private refreshResponse_() {
        const state = this.state;
        if (state.param != null) {
            this.request(state.param).then(res => {
                if (this.state !== state) return;
                if (!isErrorResponse(res)) {
                    this.setState_(state.param, res);
                } else {
                    this.setState_(state.param, undefined, new Error(res.error));
                }
            }).catch(err => {
                if (this.state !== state) return;
                this.setState_(state.param, undefined, err);
            });
        }
    }

    private setState_(param: ParamType, response?: ResponseType, error?: Error) {
        this.state = new DataRequestState(param);
        this.state.response = response;
        this.state.error = error;
        this.subscribers_.forEach(cb => cb());
    }

    subscribe(callback: () => void): () => void {
        this.subscribers_.push(callback);
        return () => {
            this.subscribers_ = this.subscribers_.filter(cb => cb !== callback);
        };
    }
}

export function useDataRequestState<ParamType, ResponseType>(request: DataRequestBase<ParamType, ResponseType>): DataRequestState<ParamType, ResponseType>;
export function useDataRequestState<ParamType, ResponseType>(request: DataRequestBase<ParamType, ResponseType> | null | undefined)
    : DataRequestState<ParamType, ResponseType> | undefined;
export function useDataRequestState<ParamType, ResponseType>(request: DataRequestBase<ParamType, ResponseType> | null | undefined)
    : DataRequestState<ParamType, ResponseType> | undefined {
    const result = useSyncExternalStore(
        (callback) => (request ? request.subscribe(callback) : (() => { })),
        () => request?.state,
        () => request?.state,
    );
    return result;
}

export const useDataRequestsState = <ParamType, ResponseType>(requests: DataRequestBase<ParamType, ResponseType>[] | null | undefined)
    : DataRequestState<ParamType, ResponseType>[] => {
    const subscribe = useCallback((callback: () => void) => {
        const unsubscribes = requests ? requests.map(req => req.subscribe(callback)) : [];
        return () => unsubscribes.forEach(unsubscribe => unsubscribe());
    }, [requests]);

    const cachedResponses = useRef<DataRequestState<ParamType, ResponseType>[]>([]);
    const get = useCallback((): DataRequestState<ParamType, ResponseType>[] => {
        const result = (() => {
            if (!requests) return [];
            return requests.map(req => req.state);
        })();
        if (cachedResponses.current.length === result.length && cachedResponses.current.every((res, i) => res === result[i])) {
            return cachedResponses.current;
        }
        cachedResponses.current = result;
        return result;
    }, [requests, cachedResponses]);
    return useSyncExternalStore(subscribe, get, get);
};