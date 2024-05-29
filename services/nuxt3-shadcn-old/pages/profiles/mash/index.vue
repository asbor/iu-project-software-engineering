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

// Define interface for mash profile
interface MashProfile {
  id: string;
  name: string;
  version: number;
  grain_temp: number;
  tun_temp: number;
  // Add more properties as needed
}

const mashProfiles = ref<MashProfile[]>([]);
const selectedMashProfile = ref<MashProfile | null>(null);

async function fetchMashProfiles() {
  try {
    const response = await fetch('http://localhost:8000/mash', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error('Failed to fetch mash profiles');
    }
    const data = await response.json();
    mashProfiles.value = data;
  } catch (error) {
    console.error(error);
  }
}

function deleteMashProfile(id: string) {
  if (!confirm('Are you sure you want to delete this mash profile?')) {
    return;
  }

  // Delete the mash profile
  fetch(`http://localhost:8000/mash/${id}`, {
    method: 'DELETE',
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to delete mash profile');
      }
      // Remove the deleted mash profile from the list
      mashProfiles.value = mashProfiles.value.filter((mashProfile) => mashProfile.id !== id);
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(fetchMashProfiles);
</script>

<template>
  <div>
    <header class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-2xl font-semibold">Mash profiles</h1>
      </div>
      <div>
        <Button asChild>
          <NuxtLink href="/mash/newMash">New mash</NuxtLink>
        </Button>
      </div>
    </header>

    <Table>
      <TableCaption>A list of your mash profiles.</TableCaption>
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
        <!-- Loop through mashProfiles and display each mash profile -->
        <template v-for="mashProfile in mashProfiles" :key="mashProfile.id">
          <TableRow>
            <TableCell>{{ mashProfile.name }}</TableCell>
            <TableCell>{{ mashProfile.version }}</TableCell>
            <TableCell>{{ mashProfile.grain_temp }}</TableCell>
            <TableCell>{{ mashProfile.tun_temp }}</TableCell>
            <TableCell class="text-right">
              <!-- Add buttons for actions like edit or delete -->
              <Button asChild class="mr-2">
                <NuxtLink :href="`/mash/${mashProfile.id}`">Edit</NuxtLink>
              </Button>

              <!-- Delete button -->
              <Button @click="deleteMashProfile(mashProfile.id)">Delete</Button>
            </TableCell>
          </TableRow>
        </template>
      </TableBody>
    </Table>
  </div>
</template>
