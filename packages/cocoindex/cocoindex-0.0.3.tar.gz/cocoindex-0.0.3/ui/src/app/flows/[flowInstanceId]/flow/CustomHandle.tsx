import React from 'react';
import { Handle, HandleProps, Position } from 'reactflow';
import classNames from 'classnames';

interface CustomHandleProps extends HandleProps {
    type: 'source' | 'target';
    position: Position;
    isConnectable?: boolean;
    text?: string;
}

const CustomHandle: React.FC<CustomHandleProps> = ({
    type,
    position,
    isConnectable = true,
    text,
    ...props
}) => {
    return (
        <Handle
            type={type}
            position={position}
            isConnectable={isConnectable}
            className={classNames(
                '!bg-[var(--gray-9)]',
                '!w-3',
                '!h-3',
                '!border-none',
                'relative',
                {
                    '!-left-4': position === Position.Left,
                    '!-right-4': position === Position.Right,
                    '!-top-4': position === Position.Top,
                    '!-bottom-4': position === Position.Bottom
                }
            )}
            {...props}
        >
            <span className='absolute text-sm top-4'>{text}</span>
        </Handle>
    );
};

export default CustomHandle;