import React from 'react';
import { Position } from 'reactflow';
import CustomHandle from './CustomHandle';
import { GoGitCommit } from "react-icons/go";
import { OpSpecView } from './OpSpec';
import { NamedSpec, TransformOpSpec } from '@/lib/spec/flow';

const OpNode = ({ data }: { data: NamedSpec<TransformOpSpec> }) => {
  return (
    <div className="OpNode rounded-lg min-w-60 w-80 max-w-80 border-2 border-[var(--gray-a6)]">

      <div className="p-2 rounded-t-lg text-center">
        <div className='flex items-center gap-2 font-bold w-full'>
          <GoGitCommit />
          <span>{data.op.kind}</span>
          <span className="flex-1"></span>
        </div>
      </div>

      <CustomHandle
        type="target"
        position={Position.Left}
      />

      <div className="flex flex-col gap-3 p-4">
        <OpSpecView data={data.op} />
      </div>

      <CustomHandle
        type="source"
        position={Position.Right}
        text={data.name}
      />
    </div>
  );
};

export default OpNode;
