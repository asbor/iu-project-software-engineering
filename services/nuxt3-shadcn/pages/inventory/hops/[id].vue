<script>
/*
Hop creation schema


*/
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      hop: {
        id: '',
        name: '',
        origin: '',
        alpha: 0,
        amount: 0,
        use: '',
        time: 0,
        notes: '',
        type: '',
        form: '',
        beta: 0,
        hsi: 0,
        display_amount: '',
        inventory: 0,
        display_time: ''
      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  mounted() {
    // Get the id of the hop profile
    this.id = this.$route.params.id;
    this.getHopProfile(this.id);
  },
  methods: {
    getHopProfile(id) {
      this.isLoading = true;
      this.isLoadingTitle = 'Loading hop...';
      // Get the hop profile
      axios.get('http://localhost:8000/hop/' + id)
        .then(res => {
          console.log(res, 'res');
          this.hop = res.data;
        })
        .catch(error => {
          console.error(error);
          // Handle error
        });
      this.isLoading = false;
    },
    updateHop() {
      this.isLoading = true;
      this.isLoadingTitle = 'Updating hop...';
      // Update the hop profile
      axios.put('http://localhost:8000/hop/' + this.id, this.hop)
        .then(res => {
          console.log(res, 'res');
          // Redirect to the previous page or perform any other action after updating
          this.$router.back();
        })
        .catch(error => {
          console.error(error);
          // Handle error
        });
      this.isLoading = false;
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
        <h1 class="text-2xl font-semibold">Edit item</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <div v-if="isLoading">
        <Loading :title="isLoadingTitle" />
      </div>
      <div v-if="!isLoading">
        <form @submit.prevent="updateHop">
          <div>
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="hop.name" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>



        </form>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="updateHop">Save</Button>
      <Button @click="cancel">Cancel</Button>
    </footer>
  </div>
</template>