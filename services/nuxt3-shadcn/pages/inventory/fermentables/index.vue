<template>
  <div>
    <header class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-2xl font-semibold">Fermentables</h1>
      </div>
      <div>
        <div class="flex gap-4">
          <Button asChild>
            <NuxtLink href="/inventory/fermentable/newFermentable">New fermentable</NuxtLink>
          </Button>
          <Button asChild>
            <BeerXMLImportFermentableDialog />
          </Button>
        </div>
      </div>
    </header>

    <Table>
      <TableCaption>A list of your fermentables.</TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead>Name</TableHead>
          <TableHead>Amount</TableHead>
          <TableHead>Cost per unit</TableHead>
          <TableHead>Supplier</TableHead>
          <TableHead>Origin</TableHead>
          <TableHead>Type</TableHead>
          <TableHead>Color</TableHead>
          <TableHead>Potential</TableHead>
          <TableHead>Yield</TableHead>
          <TableHead>Manufacturing date</TableHead>
          <TableHead>Expiry date</TableHead>
          <TableHead>Lot number</TableHead>
          <TableHead>Exclude from total</TableHead>
          <TableHead>Not fermentable</TableHead>
          <TableHead>Notes</TableHead>
          <TableHead>Description</TableHead>
          <TableHead>Substitutes</TableHead>
          <TableHead>Used in</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <!-- Loop through fermentables and display each fermentable -->
        <template v-for="fermentable in fermentables" :key="fermentable.id">
          <TableRow>
            <TableCell>{{ fermentable.name }}</TableCell>
            <TableCell>{{ fermentable.amount }}</TableCell>
            <TableCell>{{ fermentable.cost_per_unit }}</TableCell>
            <TableCell>{{ fermentable.supplier }}</TableCell>
            <TableCell>{{ fermentable.origin }}</TableCell>
            <TableCell>{{ fermentable.type }}</TableCell>
            <TableCell>{{ fermentable.color }}</TableCell>
            <TableCell>{{ fermentable.potential }}</TableCell>
            <TableCell>{{ fermentable.yield_ }}</TableCell>
            <TableCell>{{ fermentable.manufacturing_date }}</TableCell>
            <TableCell>{{ fermentable.expiry_date }}</TableCell>
            <TableCell>{{ fermentable.lot_number }}</TableCell>
            <TableCell>{{ fermentable.exclude_from_total }}</TableCell>
            <TableCell>{{ fermentable.not_fermentable }}</TableCell>
            <TableCell>{{ fermentable.notes }}</TableCell>
            <TableCell>{{ fermentable.description }}</TableCell>
            <TableCell>{{ fermentable.substitutes }}</TableCell>
            <TableCell>{{ fermentable.used_in }}</TableCell>
            <TableCell class="text-right">
              <!-- Add buttons for actions like edit or delete -->
              <Button asChild class="mr-2">
                <NuxtLink :href="`/inventory/fermentable/${fermentable.id}`">Edit</NuxtLink>
              </Button>

              <!-- Delete button -->
              <Button @click="deleteFermentable(fermentable.id)">Delete</Button>
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

// Define interface for fermentable 
interface Fermentable {
  id: string;
  name: string;
  version: number;
  grain_temp: number;
  tun_temp: number;
  // Add more properties as needed
}

const fermentables = ref<Fermentable[]>([]);
const selectedFermentable = ref<Fermentable | null>(null);

async function fetchFermentables() {
  try {
    const response = await fetch('http://localhost:8000/fermentables', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error('Failed to fetch fermentables');
    }
    const data = await response.json();
    fermentables.value = data;
  } catch (error) {
    console.error(error);
  }
}

function deleteFermentable(id: string) {
  if (!confirm('Are you sure you want to delete this fermentable?')) {
    return;
  }

  // Delete the fermentable
  fetch(`http://localhost:8000/fermentables/${id}`, {
    method: 'DELETE',
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to delete fermentable');
      }
      // Remove the deleted fermentable from the list
      fermentables.value = fermentables.value.filter((fermentable) => fermentable.id !== id);
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(fetchFermentables);
</script>