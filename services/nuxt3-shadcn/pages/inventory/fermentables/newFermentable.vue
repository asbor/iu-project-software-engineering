<template>
  <div>
    <!-- Header -->
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Create a new fermentable item</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <div v-if="isLoading">
        <Loading :title="isLoadingTitle" />
      </div>
      <div v-if="!isLoading">
        <form @submit.prevent="saveFermentable">
          <div>
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="fermentable.name" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div class="grid grid-cols-3 gap-4">
            <div>
              <label for="type">Type:</label>
              <input type="text" id="type" v-model="fermentable.type" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="yield">Yield:</label>
              <input type="number" id="yield" v-model="fermentable.yield_" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="color">Color:</label>
              <input type="number" id="color" v-model="fermentable.color" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="origin">Origin:</label>
              <input type="text" id="origin" v-model="fermentable.origin" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="supplier">Supplier:</label>
              <input type="text" id="supplier" v-model="fermentable.supplier" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="potential">Potential:</label>
              <input type="number" id="potential" v-model="fermentable.potential" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="amount">Amount:</label>
              <input type="number" id="amount" v-model="fermentable.amount" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="cost_per_unit">Cost per unit:</label>
              <input type="number" id="cost_per_unit" v-model="fermentable.cost_per_unit" required
                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="manufacturing_date">Manufacturing Date:</label>
              <input type="date" id="manufacturing_date" v-model="fermentable.manufacturing_date" required
                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="expiry_date">Expiry Date:</label>
              <input type="date" id="expiry_date" v-model="fermentable.expiry_date" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </div>
          <div>
            <label for="lot_number">Lot Number:</label>
            <input type="text" id="lot_number" v-model="fermentable.lot_number" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div class="flex items-center gap-2 mt-4 mb-2">
              <div>
                <input type="checkbox" id="exclude_from_total" v-model="fermentable.exclude_from_total"
                  class="border-2 border-gray-300 rounded-lg p-2">
              </div>
              <div>
                <label for="exclude_from_total">Exclude from total</label>
              </div>
            </div>
            <div class="flex items-center gap-2 mt-4 mb-2">
              <div>
                <input type="checkbox" id="not_fermentable" v-model="fermentable.not_fermentable"
                  class="border-2 border-gray-300 rounded-lg p-2">
              </div>
              <div>
                <label for="not_fermentable">Not fermentable</label>
              </div>
            </div>
          </div>
          <div>
            <label for="notes">Notes:</label>
            <textarea id="notes" v-model="fermentable.notes"
              class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
          <div>
            <label for="description">Description:</label>
            <textarea id="description" v-model="fermentable.description"
              class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
          <div>
            <label for="substitutes">Substitutes:</label>
            <textarea id="substitutes" v-model="fermentable.substitutes"
              class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
          <div>
            <label for="used_in">Used in:</label>
            <textarea id="used_in" v-model="fermentable.used_in"
              class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
        </form>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="saveFermentable">Save</Button>
      <Button @click="cancel">Cancel</Button>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      fermentable: {
        name: '',
        type: '',
        yield_: 0,
        color: 0,
        origin: '',
        supplier: '',
        notes: '',
        potential: 0,
        amount: 0,
        cost_per_unit: 0,
        manufacturing_date: '',
        expiry_date: '',
        lot_number: '',
        exclude_from_total: false,
        not_fermentable: false,
        description: '',
        substitutes: '',
        used_in: '',
      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  methods: {
    saveFermentable() {
      this.isLoading = true;
      this.isLoadingTitle = 'Saving...';
      axios.post('http://localhost:8000/fermentables/', this.fermentable)
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
    },
  },
};
</script>
