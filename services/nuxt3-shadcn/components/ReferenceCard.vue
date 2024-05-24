<template>
    <Card>
        <CardHeader class="px-4 pt-4 pb-1">
            <div class="flex items-center gap-2">
                <div class="yellow-400">
                    <img :src="reference.favicon_url" alt="favicon" width="20" height="20" />
                </div>
                <p>{{ reference.name }}</p>
            </div>
            <div class="text-xs flex items-center">
                <p>{{ reference.category }}</p>
            </div>
        </CardHeader>

        <CardContent class="px-4 pt-4 pb-1">
            <p><strong>Description:</strong> {{ reference.description }}</p>
        </CardContent>
        <CardFooter class="flex gap-2 py-2 px-2 items-center justify-between">
            <a :href="reference.url" target="_blank">Visit Site</a>
        </CardFooter>
    </Card>
</template>

<script setup lang="ts">
import { Card, CardContent, CardFooter, CardHeader } from '@/components/ui/card';

const props = defineProps(["reference"]);
</script>
