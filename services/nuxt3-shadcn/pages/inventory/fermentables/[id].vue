<template>
  <div>
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Edit Fermentable Item</h1>
      </div>
    </header>

    <main>
      <div v-if="isLoading">
        <Loading :title="isLoadingTitle" />
      </div>
      <div v-if="!isLoading">
        <form @submit.prevent="updateFermentable">
          <!-- Form content here -->
        </form>
      </div>
    </main>

    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="updateFermentable">Save</Button>
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
  async mounted() {
    this.id = this.$route.params.id;
    await this.getFermentableProfile(this.id);
  },
  methods: {
    async getFermentableProfile(id) {
      this.isLoading = true;
      this.isLoadingTitle = 'Loading fermentable...';
      try {
        const data = await $fetch(`http://localhost:8000/inventory/fermentables/${id}`);
        this.fermentable = data;
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async updateFermentable() {
      this.isLoading = true;
      this.isLoadingTitle = 'Updating fermentable...';
      try {
        await $fetch(`http://localhost:8000/inventory/fermentables/${this.id}`, {
          method: 'PUT',
          body: this.fermentable,
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
