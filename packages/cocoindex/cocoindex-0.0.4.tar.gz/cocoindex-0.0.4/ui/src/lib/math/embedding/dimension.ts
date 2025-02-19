export type StandardEmbeddingDimension = 64 | 128 | 256 | 384 | 512 | 768 | 1024 | 1536;
export const STANDARD_EMBEDDING_DIMENSIONS: StandardEmbeddingDimension[] = [64, 128, 256, 384, 512, 768, 1024, 1536];
export const pickEmbeddingDimension = (dimension: number): StandardEmbeddingDimension | undefined =>
    STANDARD_EMBEDDING_DIMENSIONS.find(d => d >= dimension);

export const alignEmbedding = (embedding: number[] | Float32Array | Float64Array, dimension: number): number[] => {
    const result = new Array(dimension);
    if (embedding) {
        const n = Math.min(dimension, embedding.length);
        for (let i = 0; i < n; ++i) {
            result[i] = embedding[i];
        }
    }
    return result;
};