import React from 'react';
import ReactJson from '@microlink/react-json-view';
import { useTheme } from 'next-themes';
import { OpSpec } from '@/lib/spec/flow';

export const OpSpecView = ({ data }: { data?: OpSpec }) => {
    const { resolvedTheme } = useTheme();
    const isDark = resolvedTheme === 'dark';

    if (!data) return null;

    const { kind, ...filteredData } = data;

    return (
        <ReactJson
            src={filteredData}
            theme={isDark ? "monokai" : "rjv-default"}
            name={false}
            displayDataTypes={false}
            displayObjectSize={false}
            enableClipboard={false}
        />
    );
};
