<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      yeast: {
        id: '',
        name: '',
        type: '',
        form: '',
        laboratory: '',
        product_id: '',
        min_temperature: 0,
        max_temperature: 0,
        flocculation: '',
        attenuation: 0,
        notes: '',
        best_for: '',
        max_reuse: 0,
        amount: 0,
        amount_is_weight: false,
        inventory: 0,
        display_amount: ''
      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  mounted() {
    // Get the id of the yeast profile
    this.id = this.$route.params.id;
    this.getYeastProfile(this.id);
  },
  methods: {
    getYeastProfile(id) {
      this.isLoading = true;
      this.isLoadingTitle = 'Loading yeast...';
      // Get the yeast profile
      axios.get('http://localhost:8000/inventory/yeasts/' + id)
        .then(res => {
          this.yeast = res.data;
        })
        .catch(error => {
          console.error(error);
        });
      this.isLoading = false;
    },
    updateYeast() {
      this.isLoading = true;
      this.isLoadingTitle = 'Updating yeast...';
      // Update the yeast profile
      axios.put('http://localhost:8000/inventory/yeasts/' + this.id, this.yeast)
        .then(res => {
          this.$router.back();
        })
        .catch(error => {
          console.error(error);
        });
      this.isLoading = false;
    },
    cancel() {
      this.$router.back();
    }
  }
};
</script>

<template>
  <div>
    <!-- Header -->
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Edit Yeast item</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <div v-if="isLoading">
        <Loading :title="isLoadingTitle" />
      </div>
      <div v-if="!isLoading">
        <form @submit.prevent="updateYeast">
          <div>
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="yeast.name" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label for="type">Type:</label>
              <input type="text" id="type" v-model="yeast.type" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="form">Form:</label>
              <input type="text" id="form" v-model="yeast.form" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="laboratory">Laboratory:</label>
              <input type="text" id="laboratory" v-model="yeast.laboratory" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="product_id">Product ID:</label>
              <input type="text" id="product_id" v-model="yeast.product_id" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="min_temperature">Min Temperature:</label>
              <input type="number" id="min_temperature" v-model="yeast.min_temperature" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="max_temperature">Max Temperature:</label>
              <input type="number" id="max_temperature" v-model="yeast.max_temperature" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="flocculation">Flocculation:</label>
              <input type="text" id="flocculation" v-model="yeast.flocculation" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="attenuation">Attenuation:</label>
              <input type="number" id="attenuation" v-model="yeast.attenuation" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="notes">Notes:</label>
              <textarea id="notes" v-model="yeast.notes"
                class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
            </div>
            <div>
              <label for="best_for">Best For:</label>
              <input type="text" id="best_for" v-model="yeast.best_for" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="max_reuse">Max Reuse:</label>
              <input type="number" id="max_reuse" v-model="yeast.max_reuse" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="amount">Amount:</label>
              <input type="number" id="amount" v-model="yeast.amount" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="amount_is_weight">Amount is Weight:</label>
              <input type="checkbox" id="amount_is_weight" v-model="yeast.amount_is_weight"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </div>
          <div>
            <label for="inventory">Inventory:</label>
            <input type="number" id="inventory" v-model="yeast.inventory" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="display_amount">Display Amount:</label>
            <input type="text" id="display_amount" v-model="yeast.display_amount" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
        </form>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="updateYeast">Save</Button>
      <Button @click="cancel">Cancel</Button>
    </footer>
  </div>
</template>
