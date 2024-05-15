<script setup>
import { ref } from 'vue';
import { parseString } from 'xml2js';
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
} from '@/components/ui/alert-dialog'

const { loading, open } = useHelpers();
const importedHops = ref([]);

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

    // Check if the XML contains hops
    if (!result.HOPS || !result.HOPS.HOP) {
      console.error('No hops found in BeerXML');
      return;
    }

    const hops = result.HOPS.HOP;

    // Map each hop to the format expected by importedHops
    importedHops.value = hops.map((hop) => ({
      id: uuidv4(), // Generate UUID for each hop
      name: hop.NAME[0],
      version: parseFloat(hop.VERSION[0]),
      origin: hop.ORIGIN[0],
      alpha: parseFloat(hop.ALPHA[0]),
      amount: parseFloat(hop.AMOUNT[0]),
      use: hop.USE[0],
      time: parseFloat(hop.TIME[0]),
      notes: hop.NOTES[0],
      type: hop.TYPE[0],
      form: hop.FORM[0],
      beta: parseFloat(hop.BETA[0]),
      hsi: parseFloat(hop.HSI[0]),
      display_amount: hop.DISPLAY_AMOUNT[0],
      inventory: parseFloat(hop.INVENTORY[0]),
      display_time: hop.DISPLAY_TIME[0],
    }));
  });
}
async function importHops() {
  for (const hop of importedHops.value) {
    try {
      const response = await fetch('http://localhost:8000/hop', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(hop),
      });
      if (!response.ok) {
        throw new Error('Failed to create hop');
      }
      console.log(`Hop "${hop.name}" imported successfully.`);
      // close the dialog
      open.value = false;
      window.location.reload(); // refresh the parent page
    } catch (error) {
      console.error(error);
    }
  }
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
