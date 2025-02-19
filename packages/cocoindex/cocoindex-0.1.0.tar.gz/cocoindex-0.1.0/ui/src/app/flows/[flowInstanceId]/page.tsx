'use client'

import Topbar from '@/app/components/topbar'
import { Flow } from './flow/flow'
import { Allotment } from "allotment";
import "allotment/dist/style.css";
import { TabNav } from '@radix-ui/themes'
import Serp from './serp/Serp'
import { ScrollArea } from '@radix-ui/themes'
import { IoSearchOutline } from 'react-icons/io5'
import { createSearchSession } from './dataRequests/search'
import { useCallback, useState } from 'react'
import { EmbeddingPlot } from './preview/EmbeddingPlot'
import { useParams } from 'next/navigation'
import { FlowContextProvider, useFlowContext } from './flowContext'
import { DataTable } from './preview/DataTable';

export default function Page(): JSX.Element {
    return (
        <div className='h-full w-full overflow-hidden'>
            <div className='flex flex-col h-screen'>
                <Topbar />
                <FlowContextProvider>
                    <Allotment>
                        <Allotment.Pane preferredSize={600} className='flex flex-col'>
                            <DataPane />
                        </Allotment.Pane>
                        <Allotment.Pane>
                            <RightPane />
                        </Allotment.Pane>
                    </Allotment>
                </FlowContextProvider>
            </div>
        </div>
    )
}

function DataPane(): JSX.Element {
    const searchSessions = useFlowContext(state => state.searchSessions);
    const setSearchSessions = useFlowContext(state => state.setSearchSessions);
    const activeTab = useFlowContext(state => state.activeTab);
    const setActiveTab = useFlowContext(state => state.setActiveTab);
    const params = useParams();
    const flowInstanceId = params.flowInstanceId as string;

    const addSearchSession = useCallback(() => {
        const session = createSearchSession(flowInstanceId);
        setSearchSessions([...searchSessions, session]);
        setActiveTab(session);
    }, [searchSessions, setSearchSessions, setActiveTab, flowInstanceId]);

    return (
        <>
            <TabNav.Root className="overflow-x-auto">
                <TabNav.Link
                    active={activeTab === 'preview'}
                    onClick={() => setActiveTab('preview')}
                >
                    Preview
                </TabNav.Link>
                {searchSessions.map((session, i) =>
                    <TabNav.Link
                        key={i}
                        active={activeTab === session}
                        onClick={() => setActiveTab(session)}
                    >
                        Query {i + 1}
                        <button
                            onClick={(e) => {
                                e.stopPropagation();
                                setSearchSessions(searchSessions.filter(s => s !== session));
                            }}
                            className="ml-2 hover:text-accent-9"
                        >
                            ✕
                        </button>
                    </TabNav.Link>
                )}
                <TabNav.Link onClick={addSearchSession}>
                    +<IoSearchOutline size={16} />
                </TabNav.Link>
            </TabNav.Root>
            <ScrollArea className='h-full flex w-full' scrollbars="vertical">
                {activeTab === 'preview' ? (
                    <DataTable />
                ) : (
                    <Serp searchSession={activeTab} />
                )}
            </ScrollArea>
        </>
    )
}

function RightPane(): JSX.Element {
    const [activeTab, setActiveTab] = useState<string>('flow');
    const params = useParams();
    const flowInstanceId = params.flowInstanceId as string;

    return (
        <div className='h-full flex flex-col'>
            <TabNav.Root>
                <TabNav.Link
                    active={activeTab === 'flow'}
                    onClick={() => setActiveTab('flow')}
                >
                    Configure Index
                </TabNav.Link>
                <TabNav.Link
                    active={activeTab === 'plots'}
                    onClick={() => setActiveTab('plots')}
                >
                    Plots
                </TabNav.Link>
            </TabNav.Root>
            <ScrollArea className='flex w-full' scrollbars="vertical">
                {activeTab === 'flow' ? (
                    <Flow flowInstanceId={flowInstanceId} />
                ) : (
                    <EmbeddingPlot />
                )}
            </ScrollArea>
        </div>
    )
}