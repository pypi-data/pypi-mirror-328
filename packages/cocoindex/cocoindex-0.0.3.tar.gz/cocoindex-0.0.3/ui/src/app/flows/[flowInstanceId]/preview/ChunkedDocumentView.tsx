import { CollectionValueAccessor } from "@/lib/data/accessor";
import { create, StoreApi, UseBoundStore } from "zustand";
import { useCallback, useMemo } from "react";
import { getEmbeddingSimilarity } from "@/lib/math/embedding/similarity";
import SimilarityScore from "@/app/components/similarityScore";
import { DataRequestState, useDataRequestsState } from "../dataRequests/dataRequestBase";
import { FlowInstanceQueryResponse } from "@/app/api/apiTypes";
import { SearchParams } from "../dataRequests/search";
import { useShallow } from "zustand/shallow";
import classNames from "classnames";
import { useFlowContext } from "../flowContext";
import { FlowRange } from "@/lib/data/data";
import { VECTOR_ORIGIN_TEXT } from "@/lib/spec/fieldAttrs";

export type ChunkColorTheme = 'simple' | 'colorful';

type DocumentChunk = {
    range: FlowRange;
    embedding?: number[];
    hue?: number;
};
type DocumentChunkAtom = {
    offset: number;
    text: string;
    chunks: DocumentChunk[];
};

const textToColorHue = (text: string) => {
    let hash: number = 0;
    for (let i = 0; i < text.length; i++) {
        const char = text.charCodeAt(i);
        hash ^= (hash << 3) ^ char;
    }
    const r = (hash % 360)
    return r > 0 ? r : r + 360;
};

const getDocumentChunkAtoms = (
    source: string, chunks: CollectionValueAccessor, colorTheme: ChunkColorTheme,
): DocumentChunkAtom[] => {
    const elementType = chunks.collectionType.element();

    const keyType = elementType.fieldById(0);
    if (keyType.type.type.kind != 'Range') {
        console.error('keyType is not a Range', keyType);
        return [{ offset: 0, text: source, chunks: [] }];
    }
    const rangeFieldId = 0;

    let embeddingFieldId: number | undefined;
    const fields = elementType.fields();
    for (let i = 1; i < fields.length; ++i) {
        const field = fields[i];
        if (field.attrs && VECTOR_ORIGIN_TEXT in field.attrs) {
            if (embeddingFieldId !== undefined) {
                console.warn('multiple embedding fields found, ignoring later ones', field);
            } else if (field.type.type.kind !== 'Vector') {
                console.error('embedding field is not a Vector', field);
            } else {
                embeddingFieldId = i;
            }
        }
    }

    const eventMap: Map<number, { in: DocumentChunk[], out: DocumentChunk[] }> = new Map();
    chunks.rows()?.forEach((chunkAccessor) => {
        const range = chunkAccessor.fieldById(rangeFieldId)?.value as FlowRange;
        const [start, end] = range;
        const hue = (colorTheme === 'colorful' ? textToColorHue(source.slice(start, end)) : 210);
        const embedding = embeddingFieldId !== undefined ? chunkAccessor.fieldById(embeddingFieldId)?.value as number[] : undefined;
        const chunk: DocumentChunk = { range, embedding, hue };

        {
            const event = eventMap.get(start);
            if (event) {
                event.in.push(chunk);
            } else {
                eventMap.set(start, { in: [chunk], out: [] });
            }
        }

        {
            const event = eventMap.get(end);
            if (event) {
                event.out.push(chunk);
            } else {
                eventMap.set(end, { in: [], out: [chunk] });
            }
        }

    });
    const events = Array.from(eventMap.entries()).sort(([pos0,], [pos1,]) => pos0 - pos1);

    const result: DocumentChunkAtom[] = [];
    let activeChunks: DocumentChunk[] = [];
    let lastPos = 0;
    for (const [pos, event] of events) {
        const { in: inChunks, out: outChunks } = event;
        if (pos > lastPos) {
            result.push({ offset: lastPos, text: source.slice(lastPos, pos), chunks: activeChunks });
        }

        activeChunks = activeChunks.filter(chunk => !outChunks.includes(chunk));
        inChunks.sort(({ range: [, len0] }, { range: [, len1] }) => len0 - len1);
        activeChunks.push(...inChunks);
        lastPos = pos;
    }
    if (lastPos < source.length) {
        result.push({ offset: lastPos, text: source.slice(lastPos), chunks: activeChunks });
    }

    return result;
};


type ChunkSelectionStore = {
    selectedChunk: DocumentChunk | null;
    setSelectedChunk: (chunk: DocumentChunk | null) => void;
};

export function ChunkedDocumentView({ baseText, chunks, colorTheme }: {
    baseText: string,
    chunks: CollectionValueAccessor,
    colorTheme: ChunkColorTheme,
}): JSX.Element | undefined {
    const useChunkSelectionStore =
        useMemo(() => create<ChunkSelectionStore>((set) => ({
            selectedChunk: null,
            setSelectedChunk: (chunk) => set({ selectedChunk: chunk }),
        })), []);
    const setSelectedChunk = useChunkSelectionStore(state => state.setSelectedChunk);

    const deselectChunk = useCallback(() => setSelectedChunk(null), [setSelectedChunk]);

    const searchRequests = useFlowContext(useShallow(state => state.searchSessions.map(session => session.request)));
    const searchStates = useDataRequestsState(searchRequests);
    const nonNullSearchStates = useMemo(() => searchStates.map(state => state.collapsed()).filter(state => !!state), [searchStates]);

    const chunkAtoms = getDocumentChunkAtoms(baseText, chunks, colorTheme);
    return (
        <pre className="whitespace-pre-wrap break-words relative pr-20" onClick={deselectChunk}>
            {chunkAtoms.map(atom => <PreviewDocumentChunkAtom key={atom.offset} atom={atom}
                setSelectedChunk={setSelectedChunk}
                useChunkSelectionStore={useChunkSelectionStore}
                searchStates={nonNullSearchStates}
            />)}
        </pre>
    );
}

const PreviewDocumentChunkAtom = (
    { atom, setSelectedChunk, useChunkSelectionStore, searchStates }: {
        atom: DocumentChunkAtom,
        setSelectedChunk: (chunk: DocumentChunk | null) => void,
        useChunkSelectionStore: UseBoundStore<StoreApi<ChunkSelectionStore>>,
        searchStates: DataRequestState<SearchParams, FlowInstanceQueryResponse>[],
    }): JSX.Element | undefined => {
    const selectedIndex = useChunkSelectionStore(state => state.selectedChunk ? atom.chunks.indexOf(state.selectedChunk) : -1);
    const startChunks = useMemo(() => atom.chunks.filter(({ range: [start,] }) => start === atom.offset), [atom]);
    const endChunks = useMemo(() => atom.chunks.filter(({ range: [, end] }) => end === atom.offset + atom.text.length), [atom]);

    const switchSelection = useCallback((e: React.MouseEvent) => {
        e.stopPropagation();
        if (atom.chunks.length === 0) return;
        const nextIndex = (selectedIndex + 2) % (atom.chunks.length + 1) - 1;
        setSelectedChunk(nextIndex >= 0 ? atom.chunks[nextIndex] : null);
    }, [atom, selectedIndex, setSelectedChunk]);

    const startHue = startChunks?.[0]?.hue;
    const startBorderColor = startHue ? `hsl(${startHue}, 50%, var(--chunk-bracket-lightness))` : undefined;
    const endHue = endChunks?.[0]?.hue;
    const endBorderColor = endHue ? `hsl(${endHue}, 50%, var(--chunk-bracket-lightness))` : undefined;

    const firstChar = startBorderColor ? (atom.text[0] !== '\n' ? atom.text[0] : '') : undefined;
    const firstCharAsLast = !!firstChar && !!endBorderColor && atom.text.length === 1;
    const lastChar = endBorderColor && !firstCharAsLast ? atom.text[atom.text.length - 1] : undefined;
    const remainingText = atom.text.slice(firstChar?.length ?? 0, atom.text.length - (lastChar?.length ?? 0));

    let content = (
        <span onClick={switchSelection} >
            {searchStates.length > 0 && startChunks.map((chunk, idx) => {
                const { embedding } = chunk;
                if (!embedding) return;
                const isSelected = selectedIndex >= 0 && atom.chunks[selectedIndex] === chunk;
                return (
                    <span key={idx} className={classNames("absolute right-0 text-sm flex flex-col", { "z-50": isSelected })}>
                        {
                            searchStates.map(({ param: { metric }, response }, idx) =>
                                response &&
                                <SimilarityScore key={idx} similarity={getEmbeddingSimilarity(metric, embedding, response.info.query_vector)} metric={metric} />
                            )
                        }
                    </span>
                );
            })}
            {firstChar && <span className="relative text-nowrap"><div className="absolute -left-0.5 -top-0.5 -bottom-0.5 w-2 border-l-[3px] border-t-[3px] border-b-[3px]" style={{ borderColor: startBorderColor }}></div>{firstChar}</span>}
            {remainingText}
            {(lastChar || firstCharAsLast) && <span className="relative text-nowrap">{lastChar}<div className="absolute -right-0.5 -top-0.5 -bottom-0.5 w-2 border-r-[3px] border-t-[3px] border-b-[3px]" style={{ borderColor: endBorderColor }}></div></span>}
        </span>
    );
    if (selectedIndex >= 0) {
        const selectedHue = atom.chunks[selectedIndex].hue;
        if (selectedHue) {
            content = <span style={{ backgroundColor: `hsl(${selectedHue}, 50%, var(--chunk-lightness))` }}>{content}</span>;
        }
    } else {
        for (const chunk of atom.chunks) {
            const chunkHue = chunk.hue;
            if (chunkHue) {
                content = <span style={{ backgroundColor: `hsla(${chunkHue}, 50%, var(--chunk-lightness), 0.3)` }}>{content}</span>;
            }
        }
    }
    return content;
}
