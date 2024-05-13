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
const importedFermentables = ref([]);

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

    // Check if the XML contains fermentables
    if (!result.FERMENTABLES || !result.FERMENTABLES.FERMENTABLE) {
      console.error('No fermentables found in BeerXML');
      return;
    }

    const fermentables = result.FERMENTABLES.FERMENTABLE;

    // Map each fermentable to the format expected by importedFermentables
    importedFermentables.value = fermentables.map((fermentable) => ({
      id: uuidv4(), // Generate UUID for each fermentable
      name: fermentable.NAME[0],
      amount: parseFloat(fermentable.AMOUNT[0]),
      cost_per_unit: 0, // cost not found in BeerXML, set to 0
      supplier: fermentable.SUPPLIER[0],
      origin: fermentable.ORIGIN[0],
      type: fermentable.TYPE[0],
      color: parseFloat(fermentable.COLOR[0]),
      potential: parseFloat(fermentable.POTENTIAL[0]),
      yield_: parseFloat(fermentable.YIELD[0]),
      // date fields not found in BeerXML, set to null
      manufacturing_date: "2024-12-31",
      expiry_date: "2024-12-31", // expiry date not found in BeerXML, set to empty string
      lot_number: '', // lot number not found in BeerXML, set to empty string
      exclude_from_total: false, // exclude from total not found in BeerXML, set to false
      not_fermentable: false, // not fermentable not found in BeerXML, set to false
      notes: fermentable.NOTES ? fermentable.NOTES[0] : '', // notes may not be present
      description: '', // description not found in BeerXML, set to empty string
      substitutes: '', // substitutes not found in BeerXML, set to empty string
      used_in: '', // used in not found in BeerXML, set to empty string
    }));
  });
}
async function importFermentables() {
  for (const fermentable of importedFermentables.value) {
    try {
      const response = await fetch('http://localhost:8000/fermentable', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(fermentable),
      });
      if (!response.ok) {
        throw new Error('Failed to create fermentable');
      }
      console.log(`Fermentable "${fermentable.name}" imported successfully.`);
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
      <button @click="open = true">Import Fermentables</button>
    </AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Import Fermentables from BeerXML</AlertDialogTitle>
        <input type="file" @change="handleFileChange" accept=".xml" />
        <div v-if="importedFermentables.length > 0">
          <h2>Imported Fermentables:</h2>
          <ul>
            <li v-for="fermentable in importedFermentables" :key="fermentable.id">
              {{ fermentable.name }}
            </li>
          </ul>
        </div>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
        <AlertDialogAction @click="importFermentables">Import</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
