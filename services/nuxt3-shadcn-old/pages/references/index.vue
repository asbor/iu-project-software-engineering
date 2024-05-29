<template>
    <div>
        <header class="flex justify-between items-center mb-8">
            <div>
                <h1 class="text-2xl font-semibold">References</h1>
            </div>
            <div>
                <div class="flex gap-4">
                    <Button asChild>
                        <NuxtLink href="/references/newReferences">New Reference</NuxtLink>
                    </Button>
                    <Button asChild>
                        <XMLImportReferenceDialog />
                    </Button>
                    <Button asChild>
                        <XMLExportReferenceDialog />
                    </Button>
                </div>
            </div>
        </header>

        <Table>
            <TableCaption>A list of your references.</TableCaption>
            <TableHeader>
                <TableRow>
                    <TableHead>Logo</TableHead>
                    <TableHead>Name</TableHead>
                    <TableHead>URL</TableHead>
                    <TableHead>Description</TableHead>
                    <TableHead>Category</TableHead>
                    <TableHead class="text-right">Actions</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                <template v-for="reference in references" :key="reference.id">
                    <TableRow>
                        <TableCell>
                            <img :src="reference.favicon_url || 'https://www.pivoteka-tabor.cz/favicon.ico'"
                                alt="Favicon" @error="handleFaviconError"
                                :data-default-favicon="'https://static-00.iconduck.com/assets.00/unknown-icon-2048x2048-6wlnie9m.png'"
                                style="width: 60px;">
                        </TableCell>
                        <TableCell>{{ reference.name }}</TableCell>
                        <TableCell><a :href="reference.url" target="_blank">{{ reference.url }}</a></TableCell>
                        <TableCell>{{ reference.description }}</TableCell>
                        <TableCell>{{ reference.category }}</TableCell>
                        <TableCell class="text-right">
                            <Button asChild class="mr-2">
                                <NuxtLink :href="`/references/${reference.id}`">Edit</NuxtLink>
                            </Button>
                            <Button @click="deleteReference(reference.id)">Delete</Button>
                        </TableCell>
                    </TableRow>
                </template>
            </TableBody>
        </Table>
    </div>
</template>

<script setup lang="ts">
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from '@/components/ui/table';
import { ref, onMounted } from 'vue';
import XMLImportReferenceDialog from '@/components/XML/ImportReferenceDialog.vue';
import XMLExportReferenceDialog from '@/components/XML/ExportReferenceDialog.vue';

interface Reference {
    id: number;
    name: string;
    url: string;
    description: string;
    category: string;
    favicon_url: string;
}

const references = ref<Reference[]>([]);

async function fetchReferences() {
    try {
        const response = await fetch('http://localhost:8000/references', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        });
        if (!response.ok) {
            throw new Error('Failed to fetch references');
        }
        const data = await response.json();
        references.value = data;  // Ensure references array is populated correctly
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}

function deleteReference(id: number) {
    if (!confirm('Are you sure you want to delete this reference?')) {
        return;
    }

    fetch(`http://localhost:8000/references/${id}`, {
        method: 'DELETE',
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error('Failed to delete reference');
            }
            references.value = references.value.filter((reference) => reference.id !== id);
        })
        .catch((error) => {
            console.error(error);
        });
}

function handleFaviconError(event: Event) {
    const target = event.target as HTMLImageElement;
    target.src = target.dataset.defaultFavicon || 'https://www.pivoteka-tabor.cz/favicon.ico';
}

onMounted(fetchReferences);
</script>
