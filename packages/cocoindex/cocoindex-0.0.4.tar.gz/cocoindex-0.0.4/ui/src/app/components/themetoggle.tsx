'use client'

import { useTheme } from 'next-themes'
import { useState, useEffect } from 'react'
import { DropdownMenu, Tooltip, IconButton } from '@radix-ui/themes';
import { GoSun } from 'react-icons/go';
import { LuMoon } from 'react-icons/lu';
import { MdOutlineAutoMode } from 'react-icons/md';

const ThemeToggle = (): JSX.Element | null => {
    const { setTheme, resolvedTheme } = useTheme()
    const [mounted, setMounted] = useState<boolean>(false)

    useEffect(() => {
        setMounted(true)
    }, [])

    if (!mounted) {
        return null
    }

    return (
        <DropdownMenu.Root>
            <Tooltip content="Theme">
                <DropdownMenu.Trigger>
                    <IconButton variant="ghost" size='2'>
                        {resolvedTheme === 'light' ? <GoSun /> : <LuMoon />}
                    </IconButton>
                </DropdownMenu.Trigger>
            </Tooltip>
            <DropdownMenu.Content>
                <DropdownMenu.Item onSelect={() => setTheme('light')}>
                    <GoSun /> Light
                </DropdownMenu.Item>
                <DropdownMenu.Item onSelect={() => setTheme('dark')}>
                    <LuMoon /> Dark
                </DropdownMenu.Item>
                <DropdownMenu.Item onSelect={() => setTheme('system')}>
                    <MdOutlineAutoMode /> System
                </DropdownMenu.Item>
            </DropdownMenu.Content>
        </DropdownMenu.Root>
    );
}

export default ThemeToggle;
