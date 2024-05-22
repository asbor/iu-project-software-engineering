<template>
  <div>
    <header class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-2xl font-semibold">Yeasts</h1>
      </div>
      <div>
        <div class="flex gap-4">
          <Button asChild>
            <NuxtLink href="/inventory/yeasts/newYeast">New Yeast</NuxtLink>
          </Button>
          <Button asChild>
            <BeerXMLImportYeastDialog />
          </Button>
        </div>
      </div>
    </header>

    <Table>
      <TableCaption>A list of your yeasts.</TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead>Name</TableHead>
          <TableHead>Type</TableHead>
          <TableHead>Form</TableHead>
          <TableHead>Laboratory</TableHead>
          <TableHead>Product ID</TableHead>
          <TableHead>Min Temperature</TableHead>
          <TableHead>Max Temperature</TableHead>
          <TableHead>Flocculation</TableHead>
          <TableHead>Attenuation</TableHead>
          <TableHead>Notes</TableHead>
          <TableHead>Best For</TableHead>
          <TableHead>Max Reuse</TableHead>
          <TableHead>Amount</TableHead>
          <TableHead>Amount is Weight</TableHead>
          <TableHead>Inventory</TableHead>
          <TableHead>Display Amount</TableHead>
          <TableHead class="text-right">Actions</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <template v-for="yeast in yeasts" :key="yeast.id">
          <TableRow>
            <TableCell>{{ yeast.name }}</TableCell>
            <TableCell>{{ yeast.type }}</TableCell>
            <TableCell>{{ yeast.form }}</TableCell>
            <TableCell>{{ yeast.laboratory }}</TableCell>
            <TableCell>{{ yeast.product_id }}</TableCell>
            <TableCell>{{ yeast.min_temperature }}</TableCell>
            <TableCell>{{ yeast.max_temperature }}</TableCell>
            <TableCell>{{ yeast.flocculation }}</TableCell>
            <TableCell>{{ yeast.attenuation }}</TableCell>
            <TableCell>{{ yeast.notes }}</TableCell>
            <TableCell>{{ yeast.best_for }}</TableCell>
            <TableCell>{{ yeast.max_reuse }}</TableCell>
            <TableCell>{{ yeast.amount }}</TableCell>
            <TableCell>{{ yeast.amount_is_weight }}</TableCell>
            <TableCell>{{ yeast.inventory }}</TableCell>
            <TableCell>{{ yeast.display_amount }}</TableCell>
            <TableCell class="text-right">
              <Button asChild class="mr-2">
                <NuxtLink :href="`/inventory/yeasts/${yeast.id}`">Edit</NuxtLink>
              </Button>
              <Button @click="deleteYeast(yeast.id)">Delete</Button>
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

interface Yeast {
  id: string;
  name: string;
  type: string;
  form: string;
  laboratory: string;
  product_id: string;
  min_temperature: number;
  max_temperature: number;
  flocculation: string;
  attenuation: number;
  notes: string;
  best_for: string;
  max_reuse: number;
  amount: number;
  amount_is_weight: boolean;
  inventory: number;
  display_amount: string;
}

const yeasts = ref<Yeast[]>([]);
const selectedYeast = ref<Yeast | null>(null);
const loading = ref(false);

async function fetchYeasts() {
  try {
    loading.value = true;
    const response = await fetch('http://localhost:8000/inventory/yeasts', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error('Failed to fetch yeasts');
    }
    const data = await response.json();
    yeasts.value = data;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
}

function deleteYeast(id: string) {
  if (!confirm('Are you sure you want to delete this yeast?')) {
    return;
  }

  fetch(`http://localhost:8000/inventory/yeasts/${id}`, {
    method: 'DELETE',
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to delete yeast');
      }
      yeasts.value = yeasts.value.filter((yeast) => yeast.id !== id);
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(fetchYeasts);
</script>
