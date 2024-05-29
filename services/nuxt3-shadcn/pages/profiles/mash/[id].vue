<template>
  <div>
    <!-- Header -->
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Edit mash profile</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <form @submit.prevent="updateMash">
        <div>
          <label for="name">Profile Name:</label>
          <input type="text" id="name" v-model="mash.name" required placeholder="Optional"
            class="border-2 border-gray-300 rounded-lg p-2 w-full">
        </div>
        <div class="grid grid-cols-3 gap-4">
          <div>
            <label for="version">Version:</label>
            <input type="number" id="version" v-model="mash.version" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="grain_temp">Grain Temp:</label>
            <input type="number" id="grain_temp" v-model="mash.grain_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="tun_temp">Tun Temp:</label>
            <input type="number" id="tun_temp" v-model="mash.tun_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="sparge_temp">Sparge Temp:</label>
            <input type="number" id="sparge_temp" v-model="mash.sparge_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="ph">PH:</label>
            <input type="number" id="ph" v-model="mash.ph" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="tun_weight">Tun Weight:</label>
            <input type="number" id="tun_weight" v-model="mash.tun_weight" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="tun_specific_heat">Tun Specific Heat:</label>
            <input type="number" id="tun_specific_heat" v-model="mash.tun_specific_heat" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="display_grain_temp">Display Grain Temp:</label>
            <input type="text" id="display_grain_temp" v-model="mash.display_grain_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="display_tun_temp">Display Tun Temp:</label>
            <input type="text" id="display_tun_temp" v-model="mash.display_tun_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="display_sparge_temp">Display Sparge Temp:</label>
            <input type="text" id="display_sparge_temp" v-model="mash.display_sparge_temp" required
              placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="display_tun_weight">Display Tun Weight:</label>
            <input type="text" id="display_tun_weight" v-model="mash.display_tun_weight" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="mash_steps">Mash Steps:</label>
            <input type="text" id="mash_steps" v-model="mash.mash_steps" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
        </div>
        <div class="grid w-full gap-4 mt-4">
          <label for="notes">Notes:</label>
          <div class="flex fill-current">
            <textarea id="notes" v-model="mash.notes" class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
        </div>
        <!-- Add other input fields for other attributes -->
      </form>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="updateMash">Update</Button>
      <Button @click="cancel">Cancel</Button>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';

export default {
  data() {
    return {
      mash: {
        id: '',
        name: '',
        version: 0,
        grain_temp: 0,
        tun_temp: 0,
        sparge_temp: 0,
        ph: 0,
        tun_weight: 0,
        tun_specific_heat: 0,
        //equip_adjust: false, // Initialize as a boolean value
        notes: '',
        display_grain_temp: '',
        display_tun_temp: '',
        display_sparge_temp: '',
        display_tun_weight: '',
        mash_steps: ''
      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  async mounted() {
    this.id = this.$route.params.id;
    await this.getMashProfile(this.id);
  },
  methods: {
    async getMashProfile(id) {
      // Get the mash profile
      this.isLoading = true;
      this.isLoadingTitle = 'Loading mash profile';
      try {
        const data = await $fetch(`http://localhost:8000/mash/${id}`);
        this.mash = data;
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async updateMash() {
      // Save the mash profile
      this.isLoading = true;
      this.isLoadingTitle = 'Updating mash profile';
      try {
        await $fetch(`http://localhost:8000/mash/${this.id}`, {
          method: 'PUT',
          body: this.mash,
        });
        this.$router.back();
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    cancel() {
      // Cancel the operation
      this.$router.back();
    }
  }
};
</script>
