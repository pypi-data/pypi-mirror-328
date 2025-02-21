export type SimilarityMetric = 'CosineSimilarity' | 'L2Distance' | 'InnerProduct';

export type SimilarityMetricInfo = {
    name: string;
    calculate: (n: number, a: Float32Array | number[], b: Float32Array | number[]) => number;

    // Increasing means higher similarity score means more similar.
    isIncreasing: boolean;

    // Min and max similarity on normalized embedding vectors.
    leastSimilarityNormalized: number;
    mostSimilarityNormalized: number;

    // Min and max similarity on any embedding vectors. null means unbounded.
    leastSimilarity: number | null;
    mostSimilarity: number | null;
};

const embeddingSimilarityInfo: Record<SimilarityMetric, SimilarityMetricInfo> = {
    L2Distance: {
        name: 'L2 Distance',
        calculate: (n: number, a: Float32Array | number[], b: Float32Array | number[]) => {
            let sum = 0.0;
            for (let i = 0; i < n; ++i) {
                const diff = a[i] - b[i];
                sum += diff * diff;
            }
            return Math.sqrt(sum);
        },
        isIncreasing: false,
        leastSimilarityNormalized: 2,
        mostSimilarityNormalized: 0,
        leastSimilarity: null,
        mostSimilarity: 0,
    },

    CosineSimilarity: {
        name: 'Cosine Similarity',
        calculate: (n: number, a: Float32Array | number[], b: Float32Array | number[]) => {
            let sumA = 0.0;
            let sumB = 0.0;
            let sumAB = 0.0;
            for (let i = 0; i < n; ++i) {
                sumA += a[i] * a[i];
                sumB += b[i] * b[i];
                sumAB += a[i] * b[i];
            }
            return sumAB / Math.sqrt(sumA * sumB);
        },
        isIncreasing: true,
        leastSimilarityNormalized: -1,
        mostSimilarityNormalized: 1,
        leastSimilarity: -1,
        mostSimilarity: 1,
    },

    InnerProduct: {
        name: 'Inner Product',
        calculate: (n: number, a: Float32Array | number[], b: Float32Array | number[]) => {
            let sum = 0.0;
            for (let i = 0; i < n; ++i) {
                sum += a[i] * b[i];
            }
            return sum;
        },
        isIncreasing: true,
        leastSimilarityNormalized: -1,
        mostSimilarityNormalized: 1,
        leastSimilarity: null,
        mostSimilarity: null,
    },
};

const similarityMetricNames = new Map<string, SimilarityMetric>(Object.keys(embeddingSimilarityInfo).map((k) => [k.toLowerCase(), k as SimilarityMetric]));
export const parseSimilarityMetric = (metric: string): SimilarityMetric | undefined => similarityMetricNames.get(metric.toLowerCase());

export const SIMILARITY_METRICS = Object.keys(embeddingSimilarityInfo) as SimilarityMetric[];

export const getEmbeddingSimilarity = (metric: SimilarityMetric, a: Float32Array | number[], b: Float32Array | number[]): number => {
    if (a.length !== b.length) {
        throw new Error('Embedding dimensions must match');
    }
    return embeddingSimilarityInfo[metric].calculate(a.length, a, b);
};

export const getEmbeddingSimilarityInfo = (metric: SimilarityMetric): SimilarityMetricInfo => embeddingSimilarityInfo[metric];
