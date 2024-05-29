<template>
  <div>
    <!-- Header -->
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Edit Batch</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <div v-if="isLoading">
        <Loading :title="isLoadingTitle" />
      </div>
      <div v-else>
        <form @submit.prevent="updateBatch">
          <!-- Two columns -->
          <div class="grid grid-cols-2 gap-4">
            <BatchDetails :batch="batch" class="border-2 p-4" />

            <RecipeDetails :batch="batch" class="border-2 p-4" />

            <InventoryDetails :batch="batch" class="border-2 p-4" />

            <div class="grid grid-cols-1 gap-4">
              <WaterDetails :batch="batch" class="border-2 p-4" />

              <NotesDetails :batch="batch" class="border-2 p-4" />
            </div>
          </div>
        </form>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="updateBatch">Save</Button>
      <Button @click="cancel">Cancel</Button>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import BatchDetails from '@/components/BatchDetails.vue';
import RecipeDetails from '@/components/RecipeDetails.vue';
import InventoryDetails from '@/components/InventoryDetails.vue';
import WaterDetails from '@/components/WaterDetails.vue';
import NotesDetails from '@/components/NotesDetails.vue';

export default {
  components: {
    BatchDetails,
    RecipeDetails,
    InventoryDetails,
    WaterDetails,
    NotesDetails,
  },
  data() {
    return {
      batch: {
        id: '',
        batch_name: '',
        batch_size: 0,
        brewer: '',
        brew_date: '',
        recipe: {},
        inventory_fermentables: [],
        inventory_hops: [],
        inventory_miscs: [],
        inventory_yeasts: [],
        notes: '',
        water: ''
      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  mounted() {
    // Get the id of the batch
    this.id = this.$route.params.id;
    this.getBatch(this.id);
  },
  methods: {
    async getBatch(id) {
      this.isLoading = true;
      this.isLoadingTitle = 'Loading batch...';
      try {
        // Get the batch details
        const response = await axios.get(`http://localhost:8000/batches/${id}`);
        console.log('Batch data:', response.data);  // Inspect the data structure
        this.batch = response.data;
      } catch (error) {
        console.error(error);
        // Handle error
      } finally {
        this.isLoading = false;
      }
    },
    async updateBatch() {
      this.isLoading = true;
      this.isLoadingTitle = 'Updating batch...';
      try {
        // Update the batch details
        const response = await axios.put(`http://localhost:8000/batches/${this.id}`, this.batch);
        console.log(response, 'res');
        // Redirect to the previous page or perform any other action after updating
        this.$router.back();
      } catch (error) {
        console.error(error);
        // Handle error
      } finally {
        this.isLoading = false;
      }
    },
    cancel() {
      // Cancel the operation
      console.log('Operation canceled');
      this.$router.back();
    }
  }
};
</script>
