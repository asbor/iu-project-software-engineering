<template>
  <div>
    <!-- Header -->
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Create a new hop item</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <div v-if="isLoading">
        <Loading :title="isLoadingTitle" />
      </div>
      <div v-if="!isLoading">
        <form @submit.prevent="saveHop">
          <div>
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="hop.name" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div class="grid grid-cols-3 gap-4">
            <div>
              <label for="type">Type:</label>
              <input type="text" id="type" v-model="hop.type" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="alpha">Alpha:</label>
              <input type="number" id="alpha" v-model="hop.alpha" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="beta">Beta:</label>
              <input type="number" id="beta" v-model="hop.beta" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="origin">Origin:</label>
              <input type="text" id="origin" v-model="hop.origin" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="form">Form:</label>
              <input type="text" id="form" v-model="hop.form" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="use">Use:</label>
              <input type="text" id="use" v-model="hop.use" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="hsi">HSI:</label>
              <input type="number" id="hsi" v-model="hop.hsi" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="amount">Amount:</label>
              <input type="number" id="amount" v-model="hop.amount" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="cost_per_unit">Cost per unit:</label>
              <input type="number" id="cost_per_unit" v-model="hop.cost_per_unit" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="manufacturing_date">Manufacturing Date:</label>
              <input type="date" id="manufacturing_date" v-model="hop.manufacturing_date" required
                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="expiry_date">Expiry Date:</label>
              <input type="date" id="expiry_date" v-model="hop.expiry_date" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </div>
          <div>
            <label for="lot_number">Lot Number:</label>
            <input type="text" id="lot_number" v-model="hop.lot_number" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div class="flex items-center gap-2 mt-4 mb-2">
              <div>
                <input type="checkbox" id="exclude_from_total" v-model="hop.exclude_from_total"
                  class="border-2 border-gray-300 rounded-lg p-2">
              </div>
              <div>
                <label for="exclude_from_total">Exclude from total</label>
              </div>
            </div>
            <div class="flex items-center gap-2 mt-4 mb-2">
              <div>
                <input type="checkbox" id="not_hop" v-model="hop.not_hop"
                  class="border-2 border-gray-300 rounded-lg p-2">
              </div>
              <div>
                <label for="not_hop">Not hop</label>
              </div>
            </div>
          </div>
          <div>
            <label for="notes">Notes:</label>
            <textarea id="notes" v-model="hop.notes" class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
          <div>
            <label for="description">Description:</label>
            <textarea id="description" v-model="hop.description"
              class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
          <div>
            <label for="substitutes">Substitutes:</label>
            <textarea id="substitutes" v-model="hop.substitutes"
              class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
          <div>
            <label for="used_in">Used in:</label>
            <textarea id="used_in" v-model="hop.used_in"
              class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
        </form>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="saveHop">Save</Button>
      <Button @click="cancel">Cancel</Button>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  data() {
    return {
      hop: {
        name: '',
        type: '',
        alpha: 0,
        beta: 0,
        origin: '',
        form: '',
        use: '',
        hsi: 0,
        amount: 0,
        cost_per_unit: 0,
        manufacturing_date: null,
        expiry_date: null,
        lot_number: '',
        exclude_from_total: false,
        not_hop: false,
        notes: '',
        description: '',
        substitutes: '',
        used_in: '',
        inventory: '',
        display_amount: '',
        display_time: '',
        time: 0,
      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  methods: {
    async saveHop() {
      this.isLoading = true;
      this.isLoadingTitle = 'Saving...';
      try {
        await $fetch('http://localhost:8000/inventory/hops', {
          method: 'POST',
          body: this.hop,
        });
        this.$router.back();
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    cancel() {
      this.$router.back();
    },
  },
};
</script>
