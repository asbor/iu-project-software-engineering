<template>
  <div>
    <header class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-2xl font-semibold">Batches</h1>
      </div>
      <div>
        <div class="flex gap-4">
          <Button asChild>
            <NuxtLink href="/batches/newBatch">New Batch</NuxtLink>
          </Button>
        </div>
      </div>
    </header>
    <div v-if="loading" class="text-center">Loading...</div>
    <div v-else>
      <div style="width: 1600px; height: 800px;">
        <Table style="height: 100%; width: 100%;">
          <TableCaption>A list of your batches.</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead>id</TableHead>
              <TableHead>batch name</TableHead>
              <TableHead>batch size</TableHead>
              <TableHead>created at</TableHead>
              <TableHead>actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <!-- Loop through batches and display each batch -->
            <template v-for="batch in batches" :key="batch.id">
              <TableRow>
                <TableCell>{{ batch.id }}</TableCell>
                <TableCell>{{ batch.batch_name }}</TableCell>
                <TableCell>{{ batch.batch_size }}</TableCell>
                <TableCell>{{ batch.created_at }}</TableCell>
                <TableCell class="text-right">
                  <!-- Add buttons for actions like edit or delete -->
                  <Button asChild class="mr-2">
                    <NuxtLink :href="`/batches/${batch.id}`">Edit</NuxtLink>
                  </Button>

                  <!-- Delete button -->
                  <Button @click="deleteBatch(batch.id)">Delete</Button>
                </TableCell>
              </TableRow>
            </template>
          </TableBody>
        </Table>
      </div>
    </div>
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

// Define interface for batch
interface Batch {
  id: string;
  recipe_id: string;
  batch_size: number;
  created_at: string;
  name: string;
}

const batches = ref<Batch[]>([]);
const selectedBatch = ref<Batch | null>(null);
const loading = ref(false);

async function fetchBatches() {
  try {
    loading.value = true;
    const response = await fetch('http://localhost:8000/batches', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error('Failed to fetch batches');
    }
    const data = await response.json();
    batches.value = data;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
}

function deleteBatch(id: string) {
  if (!confirm('Are you sure you want to delete this batch?')) {
    return;
  }

  // Delete the batch
  fetch(`http://localhost:8000/batches/${id}`, {
    method: 'DELETE',
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to delete batch');
      }
      // Remove the deleted batch from the list
      batches.value = batches.value.filter((batch) => batch.id !== id);
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(fetchBatches);
</script>
