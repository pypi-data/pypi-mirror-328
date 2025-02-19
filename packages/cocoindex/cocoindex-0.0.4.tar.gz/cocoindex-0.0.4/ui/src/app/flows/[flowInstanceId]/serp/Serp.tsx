'use client'

import { Badge, Button, Card, Select, TextField } from '@radix-ui/themes'
import SimilarityScore from '@/app/components/similarityScore';
import { useDataRequestState } from '../dataRequests/dataRequestBase';
import { SIMILARITY_METRICS, SimilarityMetric } from '@/lib/math/embedding/similarity';
import { IoSearchOutline } from 'react-icons/io5';
import { useCallback } from 'react';
import { SearchSession } from '../dataRequests/search';
import { useShallow } from 'zustand/shallow';
import { FlowInstanceQueryResponse } from '@/app/api/apiTypes';
import { DataValueView } from '../preview/DataValueView';

function QueryResponse({ response }: { response: FlowInstanceQueryResponse }): JSX.Element {
    const similarityMetric = response.info.similarity_metric;
    const fields = response.results.fields;
    return (
        <>
            {response.results.results.map((result, i) => (
                <Card key={i} className='my-4'>
                    <div>
                        <div className="text-right text-sm">
                            Similarity: <SimilarityScore similarity={result.score} metric={similarityMetric} />
                        </div>
                        {result.data.map((value, i) => (
                            <div key={i} className="flex">
                                <span className="w-20 flex-none">
                                    <Badge className="mr-2">{fields[i].name}</Badge>
                                </span>
                                <div className="grow">
                                    <DataValueView type={fields[i].type} value={value} maxLines={5} />
                                </div>
                            </div>
                        ))}
                    </div>
                </Card>
            ))}
        </>);
}

export default function Serp({ searchSession }: { searchSession: SearchSession }): JSX.Element {
    const [draftParams, setDraftParams] = searchSession.useDraftParams(useShallow(state => [state.value, state.setValue]));
    const handleQueryChange = (e: React.ChangeEvent<HTMLInputElement>) => { setDraftParams({ ...draftParams, query: e.target.value }) };
    const handleMetricChange = (newMetric: SimilarityMetric) => { setDraftParams({ ...draftParams, metric: newMetric }) };
    const handleSearch = useCallback(() => {
        searchSession.request.setParam({ ...draftParams });
    }, [searchSession.request, draftParams]);
    const requestState = useDataRequestState(searchSession.request).collapsed();

    return (
        <div className="w-full h-full p-4">
            <div className='p-2 pr-20'>
                <TextField.Root placeholder="Search in the index" value={draftParams.query} onChange={handleQueryChange}>
                    <TextField.Slot>
                        <IoSearchOutline size={16} />
                    </TextField.Slot>
                </TextField.Root>
                <div className="mt-2 flex gap-2 items-center">
                    Search Similarity Metrics:
                    <Select.Root value={draftParams.metric} onValueChange={handleMetricChange}>
                        <Select.Trigger />
                        <Select.Content>
                            {SIMILARITY_METRICS.map((m) => (
                                <Select.Item key={m} value={m}>{m}</Select.Item>
                            ))}
                        </Select.Content>
                    </Select.Root>
                    <Button onClick={handleSearch}>Search</Button>
                </div>
            </div>
            {requestState ? (
                <div>
                    <div>Nearest matches under {requestState.param.metric} for: {requestState.param.query}</div>
                    <div className="mt-4">
                        {requestState.response &&
                            <QueryResponse response={requestState.response} />}
                    </div>
                </div>
            ) : (
                <div>No search performed yet</div>
            )}
        </div>
    )
}
