<script setup lang="ts">
import { Badge } from '@/components/ui/badge';
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle
} from '@/components/ui/card';
const props = defineProps(["card"]);
</script>

<template>
    <Card class="bg-neutral-200">
        <CardHeader class="px-4 pt-4 pb-1">
            <div class="flex items-center gap-2">
                <div class="yellow-400">
                    <Icon size=" 20" :name=card.icon :inline="true" />
                </div>
                <p>{{ card.title }}</p>

            </div>
            <div class="text-xs flex items-center">
                <p>{{ card.author }}</p>
            </div>
        </CardHeader>

        <CardContent class="px-4 pt-4 pb-1">
            <div class="flex items-center">
                <p>{{ card.label }}</p>
            </div>
            <div class="flex items-center gap-2">
                <p>{{ card.ABV }}</p>
                <p>{{ card.OG }}</p>
                <p>{{ card.FG }}</p>
                <p>{{ card.IBU }}</p>
            </div>
            <div class="flex items-center gap-2">
                <Badge v-for='(tag, index) in card.tags' :key='index' class="bg-green-400">{{ tag }}</Badge>
            </div>
        </CardContent>
        <CardFooter class="flex gap-2 py-2 px-2 items-center justify-between">
            <div class="flex items-center gap-2">
                <Icon size="20" name="prime:thumbs-up" />
                <p>{{ card.likes }}</p>
            </div>
            <div class="flex items-center gap-2">
                <Icon size="20" name="prime:eye" />
                <p>{{ card.views }}</p>
            </div>
            <div class="flex items-center gap-2">
                <Icon size="20" name="prime:download" />
                <p>{{ card.downloads }}</p>
            </div>
        </CardFooter>
    </Card>
</template>