export type FlowRange = [start: number, end: number];
export type FlowDataKey = string | number | boolean | FlowRange | FlowDataKey[];
export type FlowDataValue = unknown;

export const displayDataKey = (key: FlowDataKey): string => {
    if (Array.isArray(key)) {
        return key.map(k => displayDataKey(k)).join(', ');
    }
    return key.toString();
};

export const dataKeyEquals = (a: FlowDataKey, b: FlowDataKey): boolean => {
    if (Array.isArray(a) && Array.isArray(b)) {
        return a.length === b.length && a.every((k, i) => dataKeyEquals(k, b[i]));
    }
    return a === b;
};

export const dataKeyToStrs = (key: FlowDataKey): string[] => {
    const result: string[] = [];
    const addPart = (part: FlowDataKey) => {
        if (Array.isArray(part)) {
            part.forEach(p => addPart(p));
        } else {
            result.push(part.toString());
        }
    }
    addPart(key);
    return result;
};

export const encodeDataKey = (key: FlowDataKey): string => {
    return dataKeyToStrs(key).map(s => encodeURIComponent(s)).join('|');
};