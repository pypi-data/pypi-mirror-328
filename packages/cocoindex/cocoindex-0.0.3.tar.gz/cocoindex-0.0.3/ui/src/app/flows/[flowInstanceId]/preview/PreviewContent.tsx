'use client'

import { CollectionValueAccessor, FieldAccessor, StructValueAccessor, ValueAccessor } from '@/lib/data/accessor'
import { ChunkedDocumentView } from './ChunkedDocumentView';
import { DataValueView } from './DataValueView';
import { CHUNK_BASE_TEXT } from '@/lib/spec/fieldAttrs';
import { AnalyzedValueMapping } from '@/lib/data/schema';

export function PreviewContent({ valueAccessor, parentAccessor }: {
    valueAccessor: ValueAccessor,
    parentAccessor: StructValueAccessor,
}): JSX.Element | undefined {
    const fieldAccessor = valueAccessor instanceof FieldAccessor ? valueAccessor : undefined;
    const chunkBaseTextField = fieldAccessor?.schema.attrs?.[CHUNK_BASE_TEXT] as AnalyzedValueMapping | undefined;

    let chunkBaseText: string | undefined;
    let chunks: CollectionValueAccessor | undefined;
    if (chunkBaseTextField?.kind === 'Field' && (chunkBaseTextField.scope_up_level ?? 0) === 0) {
        const chunkBaseTextValue = parentAccessor.fieldByIds(chunkBaseTextField.local.fields_idx)?.value;
        if (chunkBaseTextValue) {
            if (typeof chunkBaseTextValue === 'string') {
                chunkBaseText = chunkBaseTextValue;
            } else {
                console.error('chunkBaseTextValue is not a string', chunkBaseTextValue);
            }
        }
        chunks = fieldAccessor?.asCollection();
        if (!chunks) {
            console.error('chunks is not a collection', fieldAccessor);
        }
    }
    return (
        <>
            {chunkBaseText && chunks
                ? <ChunkedDocumentView baseText={chunkBaseText} chunks={chunks} colorTheme="colorful" />
                : <DataValueView type={fieldAccessor?.type.type} value={fieldAccessor?.value} />}
        </>
    )
}