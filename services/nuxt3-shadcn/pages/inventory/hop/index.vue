<template>
  <div>
    <header class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-2xl font-semibold">Hops</h1>
      </div>
      <div>
        <div class="flex gap-4">
          <Button asChild>
            <NuxtLink href="/inventory/hop/newHop">New hop</NuxtLink>
          </Button>
          <Button asChild>
            <BeerXMLImportHopDialog />
          </Button>
        </div>
      </div>
    </header>

    <Table>
      <TableCaption>A list of your hops.</TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead>id</TableHead>
          <TableHead>Name</TableHead>
          <TableHead>Origin</TableHead>
          <TableHead>Alpha</TableHead>
          <TableHead>Amount</TableHead>
          <TableHead>Use</TableHead>
          <TableHead>Time</TableHead>
          <TableHead>Notes</TableHead>
          <TableHead>Type</TableHead>
          <TableHead>Form</TableHead>
          <TableHead>Beta</TableHead>
          <TableHead>HSI</TableHead>
          <TableHead>Display Amount</TableHead>
          <TableHead>Inventory</TableHead>
          <TableHead>Display Time</TableHead>
          <TableHead class="text-right">Actions</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <!-- Loop through hops and display each hop -->
        <template v-for="hop in hops" :key="hop.id">
          <TableRow>
            <TableCell>{{ hop.id }}</TableCell>
            <TableCell>{{ hop.name }}</TableCell>
            <TableCell>{{ hop.origin }}</TableCell>
            <TableCell>{{ hop.alpha }}</TableCell>
            <TableCell>{{ hop.amount }}</TableCell>
            <TableCell>{{ hop.use }}</TableCell>
            <TableCell>{{ hop.time }}</TableCell>
            <TableCell>{{ hop.notes }}</TableCell>
            <TableCell>{{ hop.type }}</TableCell>
            <TableCell>{{ hop.form }}</TableCell>
            <TableCell>{{ hop.beta }}</TableCell>
            <TableCell>{{ hop.hsi }}</TableCell>
            <TableCell>{{ hop.display_amount }}</TableCell>
            <TableCell>{{ hop.inventory }}</TableCell>
            <TableCell>{{ hop.display_time }}</TableCell>
            <TableCell class="text-right">
              <!-- Add buttons for actions like edit or delete -->
              <Button asChild class="mr-2">
                <NuxtLink :href="`/inventory/hop/${hop.id}`">Edit</NuxtLink>
              </Button>

              <!-- Delete button -->
              <Button @click="deleteHop(hop.id)">Delete</Button>
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

// Define interface for hop 
interface Hop {
  id: string;
  name: string;
  origin: string;
  alpha: number;
  amount: number;
  use: string;
  time: number;
  notes: string;
  type: string;
  form: string;
  beta: number;
  hsi: number;
  display_amount: string;
  inventory: number;
  display_time: string;
}

const hops = ref<Hop[]>([]);
const selectedHop = ref<Hop | null>(null);

async function fetchHops() {
  try {
    const response = await fetch('http://localhost:8000/hop', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error('Failed to fetch hops');
    }
    const data = await response.json();
    hops.value = data;
  } catch (error) {
    console.error(error);
  }
}

function deleteHop(id: string) {
  if (!confirm('Are you sure you want to delete this hop?')) {
    return;
  }

  // Delete the hop
  fetch(`http://localhost:8000/hop/${id}`, {
    method: 'DELETE',
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to delete hop');
      }
      // Remove the deleted hop from the list
      hops.value = hops.value.filter((hop) => hop.id !== id);
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(fetchHops);
</script>
