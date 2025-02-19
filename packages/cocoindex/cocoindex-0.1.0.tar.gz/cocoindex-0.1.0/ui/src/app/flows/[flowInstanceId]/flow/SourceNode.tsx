import React from 'react';
import { Position } from 'reactflow';
import { NamedSpec, OpSpec } from '@/lib/spec/flow';
import CustomHandle from './CustomHandle';
import { GoStack } from "react-icons/go";
import { OpSpecView } from './OpSpec';


const SourceNode = ({ data }: { data: NamedSpec<OpSpec> }) => {
    return (
        <div className="SourceNode w-80 rounded-[999em_40px_40px_999em] border-2 border-[var(--gray-a6)] pl-16 pt-2">
            <div className="flex flex-col gap-3 p-0 pb-4 px-4">
                <div className='flex items-center gap-2 font-bold'>
                    <GoStack />
                    {data.kind}
                    <span className="flex-1"></span>
                </div>

                <OpSpecView data={data} />
            </div>
            <div className="flex items-center">
                <CustomHandle
                    type="source"
                    position={Position.Right}
                    text={data.name}
                />
            </div>
        </div>
    );
};

export default SourceNode;
