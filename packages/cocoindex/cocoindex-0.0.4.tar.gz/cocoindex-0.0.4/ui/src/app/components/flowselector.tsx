'use client'

import { Select } from '@radix-ui/themes'
import { useEffect, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import { API_URL } from '@/constants'

const FlowSelector: React.FC = () => {
    const [flows, setFlows] = useState<string[]>([])
    const [selectedFlow, setSelectedFlow] = useState<string>('')
    const router = useRouter()
    const params = useParams()
    const flowInstanceId = params?.flowInstanceId as string

    useEffect(() => {
        const fetchFlows = async () => {
            const response = await fetch(`${API_URL}/flows`)
            const data = await response.json()

            setFlows(data)

            // If we have a flowInstanceId from URL, check if it exists in data
            if (flowInstanceId) {
                const flowExists = data.some((flow: string) => flow === flowInstanceId)
                if (flowExists) {
                    setSelectedFlow(flowInstanceId)
                }
            }
            // Otherwise leave it unselected (empty string)
        }
        fetchFlows()
    }, [flowInstanceId])

    const handleFlowChange = (value: string) => {
        setSelectedFlow(value)
        router.push(`/flows/${value}`)
    }

    return (
        <Select.Root value={selectedFlow} onValueChange={handleFlowChange}>
            <Select.Trigger />
            <Select.Content>
                {flows.map((flow) => (
                    <Select.Item key={flow} value={flow}>
                        {flow}
                    </Select.Item>
                ))}
            </Select.Content>
        </Select.Root>
    )
}

export default FlowSelector
