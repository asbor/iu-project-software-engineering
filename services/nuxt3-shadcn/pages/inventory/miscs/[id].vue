<template>
  <div>
    <!-- Header -->
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Edit Misc Item</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <div v-if="isLoading">
        <Loading :title="isLoadingTitle" />
      </div>
      <div v-if="!isLoading">
        <form @submit.prevent="updateMisc">
          <div>
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="misc.name" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div class="grid grid-cols-3 gap-4">
            <div>
              <label for="type">Type:</label>
              <input type="text" id="type" v-model="misc.type" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="use">Use:</label>
              <input type="text" id="use" v-model="misc.use" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="amount">Amount:</label>
              <input type="number" id="amount" v-model="misc.amount" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="amount_is_weight">Amount is Weight:</label>
              <input type="checkbox" id="amount_is_weight" v-model="misc.amount_is_weight"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="use_for">Use For:</label>
              <input type="text" id="use_for" v-model="misc.use_for" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="time">Time:</label>
              <input type="number" id="time" v-model="misc.time" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="batch_size">Batch Size:</label>
              <input type="number" id="batch_size" v-model="misc.batch_size" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="display_amount">Display Amount:</label>
              <input type="text" id="display_amount" v-model="misc.display_amount" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="inventory">Inventory:</label>
              <input type="number" id="inventory" v-model="misc.inventory" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
            <div>
              <label for="display_time">Display Time:</label>
              <input type="text" id="display_time" v-model="misc.display_time" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </div>
          <div>
            <label for="notes">Notes:</label>
            <textarea id="notes" v-model="misc.notes" class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
        </form>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="updateMisc">Save</Button>
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
      misc: {
        name: '',
        type: '',
        use: '',
        amount: 0,
        amount_is_weight: false,
        use_for: '',
        notes: '',
        time: 0,
        display_amount: '',
        inventory: 0,
        display_time: '',
        batch_size: 0,
      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  mounted() {
    // Get the id of the misc profile
    this.id = this.$route.params.id;
    this.getMiscProfile(this.id);
  },
  methods: {
    getMiscProfile(id) {
      this.isLoading = true;
      this.isLoadingTitle = 'Loading misc...';
      axios.get('http://localhost:8000/miscs/' + id)
        .then(res => {
          this.misc = res.data;
        })
        .catch(error => {
          console.error(error);
        });
      this.isLoading = false;
    },
    updateMisc() {
      this.isLoading = true;
      this.isLoadingTitle = 'Updating misc...';
      axios.put('http://localhost:8000/miscs/' + this.id, this.misc)
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
