<template>
    <AlertDialog :open="open">
        <AlertDialogTrigger>
            <button @click="open = true">Export References</button>
        </AlertDialogTrigger>
        <AlertDialogContent>
            <AlertDialogHeader>
                <AlertDialogTitle>Export References to XML</AlertDialogTitle>
                <AlertDialogDescription>Click the button below to download an XML file of your references.
                </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
                <AlertDialogAction @click="exportReferences">Export</AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
</template>

<script setup>
import { ref } from 'vue';
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger } from '@/components/ui/alert-dialog';

const open = ref(false);

async function exportReferences() {
    try {
        const response = await fetch('http://localhost:8000/references/export', {
            method: 'GET',
            headers: {
                'Accept': 'application/xml',
            },
        });

        if (!response.ok) {
            throw new Error('Failed to export references');
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'references.xml';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    } catch (error) {
        console.error('Error exporting references:', error);
    } finally {
        open.value = false;
    }
}
</script>
