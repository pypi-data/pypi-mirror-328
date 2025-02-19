import { SimilarityMetric, SimilarityMetricInfo } from "@/lib/math/embedding/similarity";
import { getEmbeddingSimilarityInfo } from "@/lib/math/embedding/similarity";

const MAX_SATURATION = 100;
export const similarityToHueSaturation = (similarity: number, metricInfo: SimilarityMetricInfo): [number, number] => {
    // Normalize to [0, 1]
    const normalizedSimilarity = (similarity - metricInfo.leastSimilarityNormalized) / (metricInfo.mostSimilarityNormalized - metricInfo.leastSimilarityNormalized);

    if (normalizedSimilarity >= 0 && normalizedSimilarity <= 0.5) {
        return [0, Math.round((0.5 - normalizedSimilarity) * (MAX_SATURATION * 2))];
    }
    if (normalizedSimilarity > 0.5 && normalizedSimilarity <= 1) {
        return [120, Math.round((normalizedSimilarity - 0.5) * (MAX_SATURATION * 2))];
    }
    if (normalizedSimilarity > 1) {
        return [Math.round(180 - 60 / normalizedSimilarity), MAX_SATURATION];
    }
    return [Math.round(300 + 60 / (1 - normalizedSimilarity)), MAX_SATURATION];
}


export default function SimilarityScore({ similarity, metric }: { similarity: number, metric: SimilarityMetric }): JSX.Element {
    const [hue, saturation] = similarityToHueSaturation(similarity, getEmbeddingSimilarityInfo(metric));
    return <span className="rounded-md px-1 font-mono" style={{ backgroundColor: `hsl(${hue}, ${saturation}%, var(--similarity-score-lightness))` }}>{similarity.toFixed(3)}</span>;
}
