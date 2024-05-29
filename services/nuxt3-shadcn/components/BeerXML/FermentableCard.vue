<template>
    <Card>
        <CardHeader class="px-4 pt-4 pb-1">
            <div class="flex items-center gap-2">
                <div class="yellow-400">
                    <Icon size="20" :name="card.icon" :inline="true" />
                </div>
                <p>{{ card.name }}</p>
            </div>
        </CardHeader>

        <CardContent class="px-4 pt-4 pb-1">
            <div class="flex gap-2">
                <div>
                    <label>Type:</label>
                </div>
                <div class="ml-2">
                    {{ card.type }}
                </div>
            </div>
            <div class="flex gap-2">
                <div>
                    <label>Color:</label>
                </div>
                <div class="ml-2">
                    {{ card.color }}
                </div>
            </div>
            <div class="flex gap-2">
                <div>
                    <label>Origin:</label>
                </div>
                <div class="ml-2">
                    {{ card.origin }}
                </div>
            </div>
            <div class="flex gap-2">
                <div>
                    <label>Supplier:</label>
                </div>
                <div class="ml-2">
                    {{ card.supplier }}
                </div>
            </div>
            <div class="flex gap-2">
                <div>
                    <label>Yield:</label>
                </div>
                <div class="ml-2">
                    {{ card.yield }}
                </div>
            </div>
            <div class="flex gap-2">
                <div>
                    <label>Notes:</label>
                </div>
                <div class="ml-2">
                    {{ card.notes }}
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
