<template>
    <AlertDialog :open="open">
        <AlertDialogTrigger>
            <button @click="open = true">Import References</button>
        </AlertDialogTrigger>
        <AlertDialogContent>
            <AlertDialogHeader>
                <AlertDialogTitle>Import References from XML</AlertDialogTitle>
                <input type="file" @change="handleFileChange" accept=".xml" />
                <div v-if="importedReferences.length > 0">
                    <h2>Imported References:</h2>
                    <ul>
                        <li v-for="reference in importedReferences" :key="reference.id">
                            {{ reference.name }}
                        </li>
                    </ul>
                </div>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
                <AlertDialogAction @click="importReferences">Import</AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
</template>

<script setup>
import { ref } from 'vue';
import { XMLParser } from 'fast-xml-parser';
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger } from '@/components/ui/alert-dialog';

const open = ref(false);
const importedReferences = ref([]);
const selectedFile = ref(null);
const isLoading = ref(false); // Define the isLoading variable

function handleFileChange(event) {
    const file = event.target.files[0];
    if (!file) return;
    selectedFile.value = file;
    const reader = new FileReader();
    reader.onload = () => {
        const XMLContent = reader.result;
        parseXML(XMLContent);
    };
    reader.readAsText(file);
}

function parseXML(XMLContent) {
    parseString(XMLContent, (err, result) => {
        if (err) {
            console.error('Error parsing XML:', err);
            return;
        }

        if (!result.references || !result.references.reference) {
            console.error('No references found in XML');
            return;
        }

        const references = result.references.reference;

        importedReferences.value = references.map((reference) => ({
            id: reference.id ? reference.id[0] : '',
            name: reference.name ? reference.name[0] : '',
            url: reference.url ? reference.url[0] : '',
            description: reference.description ? reference.description[0] : '',
            category: reference.category ? reference.category[0] : '',
            favicon_url: reference.favicon_url ? reference.favicon_url[0] : '',
        }));
    });
}

async function importReferences() {
    if (!selectedFile.value) {
        console.error('No file selected for import');
        return;
    }

    isLoading.value = true;
    const formData = new FormData();
    formData.append('file', selectedFile.value);

    try {
        const response = await fetch('http://localhost:8000/references/import', {
            method: 'POST',
            body: formData,
        });
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Failed to import references: ${JSON.stringify(errorData)}`);
        }
        console.log('References imported successfully.');
    } catch (error) {
        console.error(error.message);
    } finally {
        isLoading.value = false;
        open.value = false;
        window.location.reload();
    }
}
</script>
