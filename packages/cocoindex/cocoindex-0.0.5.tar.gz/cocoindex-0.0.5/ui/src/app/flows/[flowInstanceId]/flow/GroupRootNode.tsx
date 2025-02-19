import React from 'react';
import { Position } from 'reactflow';
import CustomHandle from './CustomHandle';

const GroupRootNode = ({ data: _data }: { data: unknown }) => {
  return (
    <div className="OpNode rounded-lg min-w-0 border">

      <CustomHandle
        type="target"
        position={Position.Left}
      />

      <CustomHandle
        type="source"
        position={Position.Right}
      />
    </div>
  );
};

export default GroupRootNode;
