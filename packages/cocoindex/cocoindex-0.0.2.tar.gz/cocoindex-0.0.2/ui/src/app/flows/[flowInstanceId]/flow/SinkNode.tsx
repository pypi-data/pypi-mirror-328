import React from 'react';
import { Position } from 'reactflow';
import { MdOutlineDataset } from "react-icons/md";
import CustomHandle from './CustomHandle';
import { CollectOpSpec, NamedSpec } from '@/lib/spec/flow';

const SinkNode = ({ data }: { data: NamedSpec<CollectOpSpec> }) => {
    return (
        <div className="SinkNode w-80 rounded-[40px_999em_999em_40px] border-2 border-[var(--gray-a6)] pr-16 pt-2">
            <CustomHandle
                type="target"
                position={Position.Left}
            />

            <div className="flex flex-col gap-3 p-0 pb-4 px-4">
                <div className='flex items-center gap-2 font-bold'>
                    <MdOutlineDataset />
                    {data.collector_name}
                </div>
            </div>
        </div>
    );
};

export default SinkNode;
