import React from 'react';
import { Position } from 'reactflow';
import { MdOutlineDataset } from "react-icons/md";
import CustomHandle from './CustomHandle';
import { ExportOpSpec, NamedSpec } from '@/lib/spec/flow';

const ExportNode = ({ data }: { data: NamedSpec<ExportOpSpec> }) => {
    return (
        <div className="StoreNode w-80 border-2 border-[var(--gray-a6)] pr-16 pt-2">
            <CustomHandle
                type="target"
                position={Position.Left}
            />

            <div className="flex flex-col gap-3 p-0 pb-4 px-4">
                <div className='flex items-center gap-2 font-bold'>
                    <MdOutlineDataset />
                    {data.target.kind}
                </div>
                <div>instance:</div>
            </div>

            <CustomHandle
                // key={OutputBindingFieldName(key)}
                type="source"
                position={Position.Right}
            // text={key.toString()}
            />
        </div>
    );
};

export default ExportNode;
