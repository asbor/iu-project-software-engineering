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
    <Card>
        <CardHeader class="px-4 pt-4 pb-1">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                    <Icon size="40" name="mdi:beer" color="yellow" />
                    <CardTitle>{{ card.name }}</CardTitle>
                </div>
                <div class="flex items-center">
                    <p>{{ card.type }}</p>
                </div>
            </div>
            <div class="text-s flex items-center">
                <p>{{ card.brewer }}</p>
            </div>
        </CardHeader>

        <CardContent class="px-4 py-2 h-40">
            <CardDescription>
                {{ card.taste_notes }}
                {{ card.notes }}
            </CardDescription>


        </CardContent>
        <CardFooter class=" flex py-2 items-center justify-between">
            <div class="flex items-center gap-2">
                <label class="font-bold">ABV:</label>
                <p>{{ card.abv }}</p>
            </div>
            <div class="flex items-center gap-2">
                <label class="font-bold">OG:</label>
                <p>{{ card.og }}</p>
            </div>
            <div class="flex items-center gap-2">
                <label class="font-bold">FG:</label>
                <p>{{ card.fg }}</p>
            </div>
            <div class="flex items-center gap-2">
                <label class="font-bold">IBU:</label>
                <p>{{ card.ibu }}</p>
            </div>
        </CardFooter>
    </Card>
</template>