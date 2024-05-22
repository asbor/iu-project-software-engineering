<script setup>
import { ref } from 'vue';
import { parseString } from 'xml2js';
import { v4 as uuidv4 } from 'uuid';

import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
    AlertDialogTrigger,
} from '@/components/ui/alert-dialog';

const openYeast = ref(false);
const importedYeast = ref([]);
const isLoadingYeast = ref(false);

function handleFileChangeYeast(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = () => {
        const beerXMLContent = reader.result;
        parseBeerXMLYeast(beerXMLContent);
    };
    reader.readAsText(file);
}

function parseBeerXMLYeast(beerXMLContent) {
    parseString(beerXMLContent, (err, result) => {
        if (err) {
            console.error('Error parsing BeerXML:', err);
            return;
        }

        if (!result.YEASTS || !result.YEASTS.YEAST) {
            console.error('No yeast found in BeerXML');
            return;
        }

        const yeasts = result.YEASTS.YEAST;

        importedYeast.value = yeasts.map((yeast) => ({
            id: uuidv4(),
            name: yeast.NAME ? yeast.NAME[0] : '',
            type: yeast.TYPE ? yeast.TYPE[0] : '',
            form: yeast.FORM ? yeast.FORM[0] : '',
            amount: yeast.AMOUNT ? parseFloat(yeast.AMOUNT[0]) : 0,
            amount_is_weight: yeast.AMOUNT_IS_WEIGHT ? yeast.AMOUNT_IS_WEIGHT[0] === 'true' : false,
            laboratory: yeast.LABORATORY ? yeast.LABORATORY[0] : '',
            product_id: yeast.PRODUCT_ID ? yeast.PRODUCT_ID[0] : '',
            min_temperature: yeast.MIN_TEMPERATURE ? parseFloat(yeast.MIN_TEMPERATURE[0]) : null,
            max_temperature: yeast.MAX_TEMPERATURE ? parseFloat(yeast.MAX_TEMPERATURE[0]) : null,
            flocculation: yeast.FLOCCULATION ? yeast.FLOCCULATION[0] : '',
            attenuation: yeast.ATTENUATION ? parseFloat(yeast.ATTENUATION[0]) : null,
            notes: yeast.NOTES ? yeast.NOTES[0] : '',
            best_for: yeast.BEST_FOR ? yeast.BEST_FOR[0] : '',
            times_cultured: yeast.TIMES_CULTURED ? parseInt(yeast.TIMES_CULTURED[0]) : 0,
            max_reuse: yeast.MAX_REUSE ? parseInt(yeast.MAX_REUSE[0]) : 0,
        }));
    });
}

async function importYeast() {
    isLoadingYeast.value = true;
    for (const yeast of importedYeast.value) {
        try {
            const response = await fetch('http://localhost:8000/inventory/yeast', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(yeast),
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(`Failed to create yeast "${yeast.name}": ${JSON.stringify(errorData)}`);
            }
            console.log(`Yeast "${yeast.name}" imported successfully.`);
        } catch (error) {
            console.error(error.message);
        }
    }
    isLoadingYeast.value = false;
    openYeast.value = false;
    window.location.reload();
}
</script>

<template>
    <AlertDialog :open="openYeast">
        <AlertDialogTrigger>
            <button @click="openYeast = true">Import Yeast</button>
        </AlertDialogTrigger>
        <AlertDialogContent>
            <AlertDialogHeader>
                <AlertDialogTitle>Import Yeast from BeerXML</AlertDialogTitle>
                <input type="file" @change="handleFileChangeYeast" accept=".xml" />
                <div v-if="importedYeast.length > 0">
                    <h2>Imported Yeast:</h2>
                    <ul>
                        <li v-for="yeast in importedYeast" :key="yeast.id">
                            {{ yeast.name }}
                        </li>
                    </ul>
                </div>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogCancel @click="openYeast = false">Cancel</AlertDialogCancel>
                <AlertDialogAction @click="importYeast">Import</AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
</template>
