<template>
  <AlertDialog :open="open">
    <Button @click="open = true">{{ mode === 'create' ? 'Add' : 'Edit' }} Equipment</Button>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>{{ mode === 'create' ? 'Create a new Equipment' : 'Edit Equipment' }}</AlertDialogTitle>
        <Input v-model="formData.name" placeholder="Equipment name" />
        <Input v-model="formData.version" type="number" placeholder="Version" />
        <Input v-model="formData.boil_size" type="number" placeholder="Boil size" />
        <Input v-model="formData.batch_size" type="number" placeholder="Batch size" />
        <Input v-model="formData.tun_volume" type="number" placeholder="Tun volume" />
        <Input v-model="formData.tun_weight" type="number" placeholder="Tun weight" />
        <Input v-model="formData.tun_specific_heat" type="number" placeholder="Tun specific heat" />
        <Input v-model="formData.top_up_water" type="number" placeholder="Top-up water" />
        <Input v-model="formData.trub_chiller_loss" type="number" placeholder="Trub chiller loss" />
        <Input v-model="formData.evap_rate" type="number" placeholder="Evaporation rate" />
        <Input v-model="formData.boil_time" type="number" placeholder="Boil time" />
        <Input v-model="formData.lauter_deadspace" type="number" placeholder="Lauter dead space" />
        <Input v-model="formData.top_up_kettle" type="number" placeholder="Top-up kettle" />
        <Input v-model="formData.hop_utilization" type="number" placeholder="Hop utilization" />
        <Input v-model="formData.notes" placeholder="Notes" />
        <!-- Add more input fields for other equipment properties as needed -->
      </AlertDialogHeader>

      <AlertDialogFooter>
        <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
        <AlertDialogAction @click="saveEquipment">{{ mode === 'create' ? 'Create' : 'Save' }}</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { loading, open } from '../composables/helpers';

const formData = ref({
  id: null,
  name: '',
  version: 1,
  boil_size: 0,
  batch_size: 0,
  tun_volume: 0,
  tun_weight: 0,
  tun_specific_heat: 0,
  top_up_water: 0,
  trub_chiller_loss: 0,
  evap_rate: 0,
  boil_time: 0,
  calc_boil_volume: false,
  lauter_deadspace: 0,
  top_up_kettle: 0,
  hop_utilization: 0,
  notes: '',
  display_boil_size: '',
  display_batch_size: '',
  display_tun_volume: '',
  display_tun_weight: '',
  display_top_up_water: '',
  display_trub_chiller_loss: '',
  display_lauter_deadspace: '',
  display_top_up_kettle: '',
});

let mode = 'create';

const saveEquipment = async () => {
  try {
    console.log('Saving equipment...');
    loading.value = true;
    const url = mode === 'create' ? 'http://localhost:8000/equipment' : `http://localhost:8000/equipment/${formData.value.id}`;
    const method = mode === 'create' ? 'POST' : 'PUT';
    const response = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(formData.value),
    });
    if (!response.ok) {
      throw new Error(mode === 'create' ? 'Failed to create equipment' : 'Failed to save equipment');
    }
    console.log(mode === 'create' ? 'Equipment created successfully' : 'Equipment saved successfully');
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
    open.value = false;
  }
}
</script>
