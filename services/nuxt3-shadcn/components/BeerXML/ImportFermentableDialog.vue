<script setup>
import { ref } from 'vue';
import { XMLParser } from 'fast-xml-parser';

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
const importedFermentables = ref([]);
const isLoading = ref(false);
let nextId = 1;  // Initialize a counter for IDs

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
  const parser = new XMLParser();
  const result = parser.parse(beerXMLContent);

  if (!result.FERMENTABLES || !result.FERMENTABLES.FERMENTABLE) {
    console.error('No fermentables found in BeerXML');
    return;
  }

  const fermentables = result.FERMENTABLES.FERMENTABLE;

  importedFermentables.value = fermentables.map((fermentable) => ({
    id: nextId++,  // Use an integer ID
    name: fermentable.NAME || '',
    amount: fermentable.AMOUNT ? parseFloat(fermentable.AMOUNT) : 0,
    cost_per_unit: 0,
    supplier: fermentable.SUPPLIER || '',
    origin: fermentable.ORIGIN || '',
    type: fermentable.TYPE || '',
    color: fermentable.COLOR ? parseFloat(fermentable.COLOR) : 0,
    potential: fermentable.POTENTIAL ? parseFloat(fermentable.POTENTIAL) : 0,
    yield_: fermentable.YIELD ? parseFloat(fermentable.YIELD) : 0,
    manufacturing_date: "2024-12-31",
    expiry_date: "2024-12-31",
    lot_number: '',
    exclude_from_total: false,
    not_fermentable: false,
    notes: fermentable.NOTES || '',
    description: '',
    substitutes: '',
    used_in: '',
    alpha: null,
    beta: null,
    form: '',
    use: '',
    amount_is_weight: false,
    product_id: '',
    min_temperature: null,
    max_temperature: null,
    flocculation: '',
    attenuation: null,
    max_reuse: null,
    inventory: 0,
    display_amount: '',
    display_time: '',
    batch_size: null,
  }));
}

async function importFermentables() {
  isLoading.value = true;

  for (const fermentable of importedFermentables.value) {
    try {
      const response = await fetch('http://localhost:8000/inventory/fermentables', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(fermentable),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(`Failed to create fermentable "${fermentable.name}": ${JSON.stringify(errorData)}`);
      }

      console.log(`Fermentable "${fermentable.name}" imported successfully.`);
    } catch (error) {
      console.error(error);
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
      <button @click="open = true">Import Fermentables</button>
    </AlertDialogTrigger>
    <AlertDialogContent aria-describedby="dialog-description">
      <AlertDialogHeader>
        <AlertDialogTitle>Import Fermentables from BeerXML</AlertDialogTitle>
        <AlertDialogDescription id="dialog-description">
          Choose a BeerXML file to import fermentables.
        </AlertDialogDescription>
      </AlertDialogHeader>
      <input type="file" @change="handleFileChange" accept=".xml" />
      <div v-if="importedFermentables.length > 0">
        <h2>Imported Fermentables:</h2>
        <ul>
          <li v-for="fermentable in importedFermentables" :key="fermentable.id">
            {{ fermentable.name }}
          </li>
        </ul>
      </div>
      <AlertDialogFooter>
        <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
        <AlertDialogAction @click="importFermentables">Import</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
