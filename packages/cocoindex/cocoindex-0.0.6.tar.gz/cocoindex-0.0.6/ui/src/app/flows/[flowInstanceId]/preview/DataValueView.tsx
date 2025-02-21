import { FlowDataValue } from "@/lib/data/data";
import { useState } from "react";
import { Button } from "@radix-ui/themes";
import { ValueType } from "@/lib/data/schema";

const LongText = ({ text, maxLines }: { text: string, maxLines?: number }) => {
    const [showAll, setShowAll] = useState(false);
    const lines = text.split('\n');
    const hasMoreLines = maxLines != null && lines.length > maxLines;
    const displayedLines = maxLines != null && showAll ? lines : lines.slice(0, maxLines);

    return (
        <div>
            <pre className="whitespace-pre-wrap break-words">
                {displayedLines.join('\n')}
            </pre>
            {hasMoreLines && (
                <Button
                    variant="ghost"
                    size="1"
                    onClick={() => setShowAll(!showAll)}
                >
                    {showAll ? 'Show Less' : 'Show More'}
                </Button>
            )}
        </div>
    );
};

export const DataValueView = ({ type, value, maxLines }: { type?: ValueType, value: FlowDataValue, maxLines?: number }) => {
    if (value == null) {
        return '(null)';
    }
    if (type?.kind === 'Str' && typeof value === 'string') {
        return (
            <LongText text={value} maxLines={maxLines} />
        );
    }
    if (type?.kind === 'Range' && Array.isArray(value)) {
        return (
            <pre>
                [{value[0]}, {value[1]})
            </pre>
        );
    }

    const jsonString = JSON.stringify(value, null, 2);
    return (
        <pre className="whitespace-pre-wrap break-all text-ellipsis overflow-hidden" style={{ maxWidth: "100ch" }}>
            <LongText text={jsonString} maxLines={maxLines} />
        </pre>
    );
};