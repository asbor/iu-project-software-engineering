<template>
  <div>
    <header class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-2xl font-semibold">Miscs</h1>
      </div>
      <div>
        <div class="flex gap-4">
          <Button asChild>
            <NuxtLink href="/inventory/miscs/newMisc">New Misc</NuxtLink>
          </Button>
          <Button asChild>
            <BeerXMLImportMiscDialog />
          </Button>
        </div>
      </div>
    </header>

    <Table>
      <TableCaption>A list of your miscs.</TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead>Name</TableHead>
          <TableHead>Type</TableHead>
          <TableHead>Use</TableHead>
          <TableHead>Amount is Weight</TableHead>
          <TableHead>Use For</TableHead>
          <TableHead>Notes</TableHead>
          <TableHead>Amount</TableHead>
          <TableHead>Time</TableHead>
          <TableHead>Display Amount</TableHead>
          <TableHead>Inventory</TableHead>
          <TableHead>Display Time</TableHead>
          <TableHead>Batch Size</TableHead>
          <TableHead class="text-right">Actions</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <template v-for="misc in miscs" :key="misc.id">
          <TableRow>
            <TableCell>{{ misc.name }}</TableCell>
            <TableCell>{{ misc.type }}</TableCell>
            <TableCell>{{ misc.use }}</TableCell>
            <TableCell>{{ misc.amount_is_weight }}</TableCell>
            <TableCell>{{ misc.use_for }}</TableCell>
            <TableCell>{{ misc.notes }}</TableCell>
            <TableCell>{{ misc.amount }}</TableCell>
            <TableCell>{{ misc.time }}</TableCell>
            <TableCell>{{ misc.display_amount }}</TableCell>
            <TableCell>{{ misc.inventory }}</TableCell>
            <TableCell>{{ misc.display_time }}</TableCell>
            <TableCell>{{ misc.batch_size }}</TableCell>
            <TableCell class="text-right">
              <Button asChild class="mr-2">
                <NuxtLink :href="`/inventory/miscs/${misc.id}`">Edit</NuxtLink>
              </Button>
              <Button @click="deleteMisc(misc.id)">Delete</Button>
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

interface Misc {
  id: string;
  name: string;
  type: string;
  use: string;
  amount_is_weight: boolean;
  use_for: string;
  notes: string;
  amount: number;
  time: number;
  display_amount: string;
  inventory: number;
  display_time: string;
  batch_size: number;
}

const miscs = ref < Misc[] > ([]);
const selectedMisc = ref < Misc | null > (null);
const loading = ref(false);

async function fetchMiscs() {
  try {
    loading.value = true;
    const response = await fetch('http://localhost:8000/miscs', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error('Failed to fetch miscs');
    }
    const data = await response.json();
    miscs.value = data;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
}

function deleteMisc(id: string) {
  if (!confirm('Are you sure you want to delete this misc?')) {
    return;
  }

  fetch(`http://localhost:8000/miscs/${id}`, {
    method: 'DELETE',
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to delete misc');
      }
      miscs.value = miscs.value.filter((misc) => misc.id !== id);
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(fetchMiscs);
</script>
