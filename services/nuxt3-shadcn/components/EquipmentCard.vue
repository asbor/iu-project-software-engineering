<script setup lang="ts">
import { ref } from 'vue';
import { defineProps } from 'vue';
import { Card, CardContent, CardFooter, CardHeader } from '@/components/ui/card';
import { useRouter } from 'vue-router'; // Import Vue Router
import EquipmentEditDialog from '@/components/equipment/EditDialog.vue'; // Import EquipmentEditDialog component

const props = defineProps({
  card: Object
});

const loading = ref(false);
const formData = ref({ id: '' });

const router = useRouter(); // Initialize Vue Router

async function deleteEquipment() {
  try {
    loading.value = true;
    formData.value.id = props.card.id;
    const url = `http://localhost:8000/equipment/${formData.value.id}`;
    const response = await fetch(url, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error('Failed to delete equipment');
    }
    console.log('Equipment deleted successfully');
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
}

function editEquipment() {
}
</script>

<template>
  <Card v-if="props.card" class="rounded-lg shadow-md border border-gray-200 overflow-hidden">
    <CardHeader class="px-4 pt-4 pb-2 bg-gray-100">
      <div>
        <p class="text-lg font-semibold text-gray-800">Equipment Details</p>
      </div>
    </CardHeader>
    <CardContent class="border-b">
      <div class="px-4 py-2">
        <p class="text-gray-600"><strong>ID:</strong> {{ props.card.id }}</p>
        <p class="text-gray-600"><strong>Name:</strong> {{ props.card.name }}</p>
      </div>
      <div class="px-4 py-2">
        <p class="text-gray-600"><strong>Boil Size:</strong> {{ props.card.display_boil_size }}</p>
        <p class="text-gray-600"><strong>Boil Time:</strong> {{ props.card.boil_time }}</p>
      </div>
      <div class="px-4 py-2">
        <p class="text-gray-600"><strong>Notes:</strong> {{ props.card.notes }}</p>
      </div>
    </CardContent>
    <CardFooter class="flex justify-end px-4 py-2 bg-gray-100">
      <button @click="deleteEquipment" class="text-red-500 hover:text-red-700 font-semibold">Delete</button>
      <equipmentEditDialog />
      <EditDialog :formData="props.card" />
    </CardFooter>
  </Card>
</template>
