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
          <!-- Form content here -->
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
import { useRouter, useRoute } from 'vue-router';
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
  async mounted() {
    this.id = this.$route.params.id;
    await this.getBatch(this.id);
  },
  methods: {
    async getBatch(id) {
      this.isLoading = true;
      this.isLoadingTitle = 'Loading batch...';
      try {
        const data = await $fetch(`http://localhost:8000/batches/${id}`);
        this.batch = data;
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async updateBatch() {
      this.isLoading = true;
      this.isLoadingTitle = 'Updating batch...';
      try {
        await $fetch(`http://localhost:8000/batches/${this.id}`, {
          method: 'PUT',
          body: this.batch,
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
    }
  }
};
</script>
