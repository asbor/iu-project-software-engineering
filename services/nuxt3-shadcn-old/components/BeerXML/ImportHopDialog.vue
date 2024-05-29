<script setup>
import { ref } from 'vue';
import { XMLParser } from 'fast-xml-parser';
import { v4 as uuidv4 } from 'uuid';

// Assuming these components are imported correctly
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from '@/components/ui/alert-dialog';

const open = ref(false);
const importedHops = ref([]);
const isLoading = ref(false);

function handleFileChange(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = () => {
    const beerXMLContent = reader.result;
    parseBeerXML(beerXMLContent);
  };
  reader.readAsText(file);
}

function parseBeerXML(beerXMLContent) {
  parseString(beerXMLContent, (err, result) => {
    if (err) {
      console.error('Error parsing BeerXML:', err);
      return;
    }

    if (!result.HOPS || !result.HOPS.HOP) {
      console.error('No hops found in BeerXML');
      return;
    }

    const hops = result.HOPS.HOP;

    importedHops.value = hops.map((hop) => ({
      id: uuidv4(),
      name: hop.NAME ? hop.NAME[0] : '',
      amount: hop.AMOUNT ? parseFloat(hop.AMOUNT[0]) : 0,
      cost_per_unit: 0,
      supplier: hop.SUPPLIER ? hop.SUPPLIER[0] : '',
      origin: hop.ORIGIN ? hop.ORIGIN[0] : '',
      type: hop.TYPE ? hop.TYPE[0] : '',
      color: hop.COLOR ? parseFloat(hop.COLOR[0]) : 0,
      potential: hop.POTENTIAL ? parseFloat(hop.POTENTIAL[0]) : 0,
      yield_: hop.YIELD ? parseFloat(hop.YIELD[0]) : 0,
      manufacturing_date: "2024-12-31",
      expiry_date: "2024-12-31",
      lot_number: '',
      exclude_from_total: false,
      not_hop: false,
      notes: hop.NOTES ? hop.NOTES[0] : '',
      description: '',
      substitutes: '',
      used_in: '',
      alpha: hop.ALPHA ? parseFloat(hop.ALPHA[0]) : 0,
      beta: hop.BETA ? parseFloat(hop.BETA[0]) : 0,
      form: hop.FORM ? hop.FORM[0] : '',
      use: hop.USE ? hop.USE[0] : '',
      amount_is_weight: false,
      product_id: '',
      min_temperature: null,
      max_temperature: null,
      flocculation: '',
      attenuation: null,
      max_reuse: null,
      inventory: hop.INVENTORY ? hop.INVENTORY[0] : '',
      display_amount: '',
      display_time: '',
      batch_size: null,
      hsi: hop.HSI ? parseFloat(hop.HSI[0]) : 0,  // Ensure hsi field is present
      time: hop.TIME ? parseInt(hop.TIME[0]) : 0,  // Ensure time field is present
    }));
  });
}

async function importHops() {
  isLoading.value = true;
  for (const hop of importedHops.value) {
    try {
      const response = await fetch('http://localhost:8000/inventory/hops', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(hop),
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(`Failed to create hop "${hop.name}": ${JSON.stringify(errorData)}`);
      }
      console.log(`Hop "${hop.name}" imported successfully.`);
    } catch (error) {
      console.error(error.message);
    }
  }
  isLoading.value = false;
  open.value = false;
  window.location.reload();
}
</script>

<template>
  <AlertDialog :open="open">
    <AlertDialogTrigger>
      <button @click="open = true">Import Hops</button>
    </AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Import Hops from BeerXML</AlertDialogTitle>
        <input type="file" @change="handleFileChange" accept=".xml" />
        <div v-if="importedHops.length > 0">
          <h2>Imported Hops:</h2>
          <ul>
            <li v-for="hop in importedHops" :key="hop.id">
              {{ hop.name }}
            </li>
          </ul>
        </div>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
        <AlertDialogAction @click="importHops">Import</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
