'use client'

import { RadioCards, Text } from '@radix-ui/themes'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { API_URL } from '@/constants'

const FlowList: React.FC = () => {
    const [flows, setFlows] = useState<string[]>([])
    const router = useRouter()

    useEffect(() => {
        const fetchFlows = async () => {
            const response = await fetch(`${API_URL}/flows`)
            const data = await response.json()
            setFlows(data)
        }
        fetchFlows()
    }, [])

    const handleFlowSelect = (value: string) => {
        router.push(`/flows/${value}`)
    }

    return (
        <RadioCards.Root onValueChange={handleFlowSelect}>
            {flows.map((flow) => (
                <RadioCards.Item key={flow} value={flow}>
                    <Text size="2">{flow}</Text>
                </RadioCards.Item>
            ))}
        </RadioCards.Root>
    )
}

export default FlowList
