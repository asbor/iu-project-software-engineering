<script setup>
import { ref } from 'vue';
import { XMLParser } from 'fast-xml-parser';

// Assuming these components are imported correctly
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
let nextId = 1;  // Initialize a counter for IDs

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
    const parser = new XMLParser();
    const result = parser.parse(beerXMLContent);

    if (!result.YEASTS || !result.YEASTS.YEAST) {
        console.error('No yeast found in BeerXML');
        return;
    }

    const yeasts = result.YEASTS.YEAST;

    importedYeast.value = yeasts.map((yeast) => ({
        id: nextId++,  // Use an integer ID
        name: yeast.NAME || '',
        type: yeast.TYPE || '',
        form: yeast.FORM || '',
        amount: yeast.AMOUNT ? parseFloat(yeast.AMOUNT) : 0,
        amount_is_weight: yeast.AMOUNT_IS_WEIGHT === 'true',
        laboratory: yeast.LABORATORY || '',
        product_id: yeast.PRODUCT_ID || '',
        min_temperature: yeast.MIN_TEMPERATURE ? parseFloat(yeast.MIN_TEMPERATURE) : null,
        max_temperature: yeast.MAX_TEMPERATURE ? parseFloat(yeast.MAX_TEMPERATURE) : null,
        flocculation: yeast.FLOCCULATION || '',
        attenuation: yeast.ATTENUATION ? parseFloat(yeast.ATTENUATION) : null,
        notes: yeast.NOTES || '',
        best_for: yeast.BEST_FOR || '',
        times_cultured: yeast.TIMES_CULTURED ? parseInt(yeast.TIMES_CULTURED) : 0,
        max_reuse: yeast.MAX_REUSE ? parseInt(yeast.MAX_REUSE) : 0,
    }));
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
