export type ErrorResponse = {
    error: string;
};

export const isErrorResponse = (response: unknown): response is ErrorResponse => {
    return typeof response === 'object' && response !== null && 'error' in response;
};