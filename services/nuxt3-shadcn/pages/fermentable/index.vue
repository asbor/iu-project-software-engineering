<template>
  <div>
    <header class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-2xl font-semibold">Fermentable profiles</h1>
      </div>
      <div>
        <Button asChild>
          <NuxtLink href="/fermentable/newFermentable">New fermentable</NuxtLink>
        </Button>
      </div>
    </header>

    <Table>
      <TableCaption>A list of your fermentable profiles.</TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead>Name</TableHead>
          <TableHead>Version</TableHead>
          <TableHead>Grain Temp</TableHead>
          <TableHead>Tun Temp</TableHead>
          <TableHead class="text-right">Actions</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <!-- Loop through fermentableProfiles and display each fermentable profile -->
        <template v-for="fermentableProfile in fermentableProfiles" :key="fermentableProfile.id">
          <TableRow>
            <TableCell>{{ fermentableProfile.name }}</TableCell>
            <TableCell>{{ fermentableProfile.version }}</TableCell>
            <TableCell class="text-right">
              <!-- Add buttons for actions like edit or delete -->
              <Button asChild class="mr-2">
                <NuxtLink :href="`/fermentable/${fermentableProfile.id}`">Edit</NuxtLink>
              </Button>

              <!-- Delete button -->
              <Button @click="deleteFermentableProfile(fermentableProfile.id)">Delete</Button>
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

// Define interface for fermentable profile
interface FermentableProfile {
  id: string;
  name: string;
  version: number;
  grain_temp: number;
  tun_temp: number;
  // Add more properties as needed
}

const fermentableProfiles = ref<FermentableProfile[]>([]);
const selectedFermentableProfile = ref<FermentableProfile | null>(null);

async function fetchFermentableProfiles() {
  try {
    const response = await fetch('http://localhost:8000/fermentable', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error('Failed to fetch fermentable profiles');
    }
    const data = await response.json();
    fermentableProfiles.value = data;
  } catch (error) {
    console.error(error);
  }
}

function deleteFermentableProfile(id: string) {
  if (!confirm('Are you sure you want to delete this fermentable profile?')) {
    return;
  }

  // Delete the fermentable profile
  fetch(`http://localhost:8000/fermentable/${id}`, {
    method: 'DELETE',
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to delete fermentable profile');
      }
      // Remove the deleted fermentable profile from the list
      fermentableProfiles.value = fermentableProfiles.value.filter((fermentableProfile) => fermentableProfile.id !== id);
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(fetchFermentableProfiles);
</script>
