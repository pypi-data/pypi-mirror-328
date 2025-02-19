'use client';

import FlowList from './components/flowlist';
import { Heading } from '@radix-ui/themes';

export default function Page() {
    return (
        <div className="h-screen w-full flex flex-col items-center justify-center">
            <div>
                <Heading size="6" className='m-4'>Select a flow to start</Heading>
            </div>
            <FlowList />
        </div>
    );
}
