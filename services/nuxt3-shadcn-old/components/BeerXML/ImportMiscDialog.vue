<script setup>
import { ref } from 'vue';
import { XMLParser } from 'fast-xml-parser';
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

const openMisc = ref(false);
const importedMisc = ref([]);
const isLoadingMisc = ref(false);

function handleFileChangeMisc(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = () => {
        const beerXMLContent = reader.result;
        parseBeerXMLMisc(beerXMLContent);
    };
    reader.readAsText(file);
}

function parseBeerXMLMisc(beerXMLContent) {
    parseString(beerXMLContent, (err, result) => {
        if (err) {
            console.error('Error parsing BeerXML:', err);
            return;
        }

        if (!result.MISCS || !result.MISCS.MISC) {
            console.error('No misc found in BeerXML');
            return;
        }

        const miscs = result.MISCS.MISC;

        importedMisc.value = miscs.map((misc) => ({
            id: uuidv4(),
            name: misc.NAME ? misc.NAME[0] : '',
            amount: misc.AMOUNT ? parseFloat(misc.AMOUNT[0]) : 0,
            type: misc.TYPE ? misc.TYPE[0] : '',
            use: misc.USE ? misc.USE[0] : '',
            time: misc.TIME ? parseInt(misc.TIME[0]) : 0,
            notes: misc.NOTES ? misc.NOTES[0] : '',
        }));
    });
}

async function importMisc() {
    isLoadingMisc.value = true;
    for (const misc of importedMisc.value) {
        try {
            const response = await fetch('http://localhost:8000/inventory/misc', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(misc),
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(`Failed to create misc "${misc.name}": ${JSON.stringify(errorData)}`);
            }
            console.log(`Misc "${misc.name}" imported successfully.`);
        } catch (error) {
            console.error(error.message);
        }
    }
    isLoadingMisc.value = false;
    openMisc.value = false;
    window.location.reload();
}
</script>

<template>
    <AlertDialog :open="openMisc">
        <AlertDialogTrigger>
            <button @click="openMisc = true">Import Misc</button>
        </AlertDialogTrigger>
        <AlertDialogContent>
            <AlertDialogHeader>
                <AlertDialogTitle>Import Misc from BeerXML</AlertDialogTitle>
                <input type="file" @change="handleFileChangeMisc" accept=".xml" />
                <div v-if="importedMisc.length > 0">
                    <h2>Imported Misc:</h2>
                    <ul>
                        <li v-for="misc in importedMisc" :key="misc.id">
                            {{ misc.name }}
                        </li>
                    </ul>
                </div>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogCancel @click="openMisc = false">Cancel</AlertDialogCancel>
                <AlertDialogAction @click="importMisc">Import</AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
</template>
