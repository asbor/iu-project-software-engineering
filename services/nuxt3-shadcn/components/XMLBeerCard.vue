<template>
    <Card>
        <CardHeader class="px-4 pt-4 pb-1">
            <div class="flex items-center gap-2">
                <div class="yellow-400">
                    <Icon size=" 20" :name="card.icon" :inline="true" />
                </div>
                <p>{{ card.name }}</p>
            </div>
            <div class="text-xs flex items-center">
                <p>{{ card.brewer }}</p>
            </div>
            <div class="flex items-center">
                <p>{{ card.type }}</p>
            </div>
        </CardHeader>

        <CardContent class="px-4 pt-4 pb-1">
            <p><strong>Batch Size:</strong> {{ formatVolume(card.batchSize) }}</p>
            <div>
                <div class="flex items-center gap-2">
                    <strong>Hops:</strong> {{ Array.from(new Set(card.hops.map(hop => hop.name))).join(', ') }}
                </div>
                <div class="flex items-center gap-2">
                    <strong>Fermentables:</strong> {{ Array.from(new Set(card.fermentables.map(fermentable =>
                        fermentable.name))).join(', ') }}
                </div>
                <div class="flex items-center gap-2">
                    <strong>Misc:</strong> {{ Array.from(new Set(card.miscs.map(misc => misc.name))).join(', ') }}
                </div>
                <div class="flex items-center gap-2">
                    <strong>Yeast:</strong> {{ Array.from(new Set(card.yeasts.map(yeast => yeast.name))).join(', ') }}
                </div>
                <div class="flex items-center gap-2">
                    <strong>styles:</strong> {{ Array.from(new Set(card.styles.map(style => style.name))).join(', ') }}
                </div>
                <div class="flex items-center gap-2">
                    <strong>Notes:</strong> {{ Array.from(new Set(card.styles.map(style => style.notes))).join(', ') }}
                </div>
            </div>
            <div class="flex items-center gap-2">
                <Badge v-for='(tag, index) in card.tags' :key='index' class="bg-green-400">{{ tag }}</Badge>
            </div>
        </CardContent>
        <CardFooter class="flex gap-2 py-2 px-2 items-center justify-between">
        </CardFooter>
    </Card>
</template>

<script setup lang="ts">
import { Badge } from '@/components/ui/badge';
import { Card, CardContent, CardFooter, CardHeader } from '@/components/ui/card';

const props = defineProps(["card"]);

const formatDensity = (value) => {
    return `${parseFloat(value).toFixed(2)} °P`;
};

const formatVolume = (value) => {
    return `${parseFloat(value).toFixed(2)} L`;
};
</script>
