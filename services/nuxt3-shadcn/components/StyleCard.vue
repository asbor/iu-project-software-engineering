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
const props = defineProps(["style"]);
</script>

<template>
    <Card>
        <CardHeader class="px-4 pt-4 pb-1">
            <div class="flex gap-2">
                <strong>{{ style.category }}</strong>
            </div>
        </CardHeader>
        <CardContent class="px-4 pt-4 pb-1">
            <div class="flex">
                <strong class="text-bold">Color:&nbsp;</strong>
                <p>{{ style.color }}</p>
            </div>
            <div class="flex">
                <strong class="text-bold">Clarity:&nbsp;</strong>
                <p>{{ style.clarity }}</p>
            </div>
            <div class="flex">
                <strong class="text-bold">Perceived Malt Aroma & Flavor:&nbsp;</strong>
                <p>{{ style.perceived_malt_and_aroma }}</p>
            </div>
            <div class="flex">
                <strong class="text-bold">Perceived Hop Aroma & Flavor:&nbsp;</strong>
                <p>{{ style.perceived_hop_and_aroma }}</p>
            </div>
            <div class="flex">
                <strong class="text-bold">Perceived Bitterness:&nbsp;</strong>
                <p>{{ style.perceived_bitterness }}</p>
            </div>
            <div class="flex">
                <strong class="text-bold">Fermentation Characteristics:&nbsp;</strong>
                <p>{{ style.fermentation_characteristics }}</p>
            </div>
            <div class="flex">
                <strong class="text-bold">Body:&nbsp;</strong>
                <p>{{ style.body }}</p>
            </div>
            <div class="flex">
                <strong class="text-bold">Additional notes:&nbsp;</strong>
                <p>{{ style.additional_notes }}</p>
            </div>
        </CardContent>
        <CardFooter class="text-xs flex gap-2 py-2 px-2 justify-between">
            <div>
                <strong class="text-bold">Original Gravity [OG]:&nbsp;</strong>
                <p>{{ style.og }}</p>
            </div>
            <div>
                <strong class="text-bold">Final Gravity [FG]:&nbsp;</strong>
                <p>{{ style.fg }}</p>
            </div>
            <div>
                <strong class="text-bold">Alcohol by Volume [ABV]:&nbsp;</strong>
                <p>{{ style.abv }}</p>
            </div>
            <div>
                <strong class="text-bold">Bitterness [IBU]:&nbsp;</strong>
                <p>{{ style.ibu }}</p>
            </div>
            <div>
                <strong class="text-bold">Color SRM [EBC]:&nbsp;</strong>
                <p>{{ style.ebc }}</p>
            </div>
        </CardFooter>
    </Card>
</template>