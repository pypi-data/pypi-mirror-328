'use client'

import Image from 'next/image'
import { Separator } from '@radix-ui/themes'
import ThemeToggle from './themetoggle'
import FlowSelector from './flowselector'

const Topbar: React.FC = () => {
    return (
        <div className="w-full">
            <div className='h-10 flex items-center px-4 w-full'>
                <Image
                    src="/icon.svg"
                    alt="CocoIndex Logo"
                    width={24}
                    height={24}
                    className='object-contain'
                />

                <div className='flex-grow ml-8'>
                    <FlowSelector />
                </div>
                <div className='mr-8 mt-2'>
                    <ThemeToggle />
                </div>
            </div>
            <Separator orientation="horizontal" size="4" />
        </div>
    )
}

export default Topbar
