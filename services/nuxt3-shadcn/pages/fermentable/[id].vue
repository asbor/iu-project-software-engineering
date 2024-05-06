<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      fermentable: {
        id: '',
        name: '',
        version: 0,
        grain_temp: 0,
        tun_temp: 0,
        sparge_temp: 0,
        ph: 0,
        tun_weight: 0,
        tun_specific_heat: 0,
        notes: '',
        display_grain_temp: '',
        display_tun_temp: '',
        display_sparge_temp: '',
        display_tun_weight: '',
        mash_steps: ''
      },
    };
  },
  mounted() {
    // Get the id of the fermentable profile
    this.id = this.$route.params.id;
    this.getFermentableProfile(this.id);
  },
  methods: {
    getFermentableProfile(id) {
      // Get the fermentable profile
      axios.get('http://localhost:8000/fermentable/' + id)
        .then(res => {
          console.log(res, 'res');
          this.fermentable = res.data;
        })
        .catch(error => {
          console.error(error);
          // Handle error
        });
    },
    updateFermentable() {
      // Update the fermentable profile
      axios.put('http://localhost:8000/fermentable/' + this.id, this.fermentable)
        .then(res => {
          console.log(res, 'res');
          // Redirect to the previous page or perform any other action after updating
          this.$router.back();
        })
        .catch(error => {
          console.error(error);
          // Handle error
        });
    },
    cancel() {
      // Cancel the operation
      console.log('Operation canceled');
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
        <h1 class="text-2xl font-semibold">Edit fermentable profile</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <form @submit.prevent="updateFermentable">
        <div>
          <label for="name">Profile Name:</label>
          <input type="text" id="name" v-model="fermentable.name" required placeholder="Optional"
            class="border-2 border-gray-300 rounded-lg p-2 w-full">
        </div>
        <div class="grid grid-cols-3 gap-4">
          <div>
            <label for="version">Version:</label>
            <input type="number" id="version" v-model="fermentable.version" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="grain_temp">Grain Temp:</label>
            <input type="number" id="grain_temp" v-model="fermentable.grain_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="tun_temp">Tun Temp:</label>
            <input type="number" id="tun_temp" v-model="fermentable.tun_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="sparge_temp">Sparge Temp:</label>
            <input type="number" id="sparge_temp" v-model="fermentable.sparge_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="ph">PH:</label>
            <input type="number" id="ph" v-model="fermentable.ph" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="tun_weight">Tun Weight:</label>
            <input type="number" id="tun_weight" v-model="fermentable.tun_weight" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="tun_specific_heat">Tun Specific Heat:</label>
            <input type="number" id="tun_specific_heat" v-model="fermentable.tun_specific_heat" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>


          <div>
            <label for="display_grain_temp">Display Grain Temp:</label>
            <input type="text" id="display_grain_temp" v-model="fermentable.display_grain_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="display_tun_temp">Display Tun Temp:</label>
            <input type="text" id="display_tun_temp" v-model="fermentable.display_tun_temp" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="display_sparge_temp">Display Sparge Temp:</label>
            <input type="text" id="display_sparge_temp" v-model="fermentable.display_sparge_temp" required
              placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="display_tun_weight">Display Tun Weight:</label>
            <input type="text" id="display_tun_weight" v-model="fermentable.display_tun_weight" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <div>
            <label for="mash_steps">Mash Steps:</label>
            <input type="text" id="mash_steps" v-model="fermentable.mash_steps" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>


        </div>
        <div class="grid w-full gap-4 mt-4">
          <label for="notes">Notes:</label>
          <div class="flex fill-current">
            <textarea id="notes" v-model="fermentable.notes" class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
          </div>
        </div>
        <!-- Add other input fields for other attributes -->
      </form>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="updateFermentable">Update</Button>
      <Button @click="cancel">Cancel</Button>
    </footer>
  </div>
</template>
