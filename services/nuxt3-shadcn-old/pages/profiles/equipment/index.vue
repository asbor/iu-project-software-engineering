<template>
  <div class="grid w-full gap-4">
    <header class="flex items-start justify-between">
      <div class="grow">
        <p>Hi, welcome back !</p>
        <h1>Dashboard</h1>
      </div>
      <equipmentNewDialog />
    </header>
    <main>
      <div class="grid gap-4 lg:grid-cols-4">
        <!-- Loop through the equipment data and display cards -->
        <EquipmentCard v-for="(item, index) in equipment" :card="item" :key="index"
          @editEquipment="openEditDialog(item)" />

      </div>
    </main>
    <footer>
      <nuxt-link to="/">Home</nuxt-link>
    </footer>
    <!-- Add the edit dialog here -->
    <EditDialog v-if="selectedEquipment" :equipment="selectedEquipment" @close="selectedEquipment = null" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      equipment: [], // Array to hold equipment data
      selectedEquipment: null // Store the selected equipment item
    };
  },
  async created() {
    await this.fetchEquipment(); // Fetch equipment data when component is created
  },
  methods: {
    async fetchEquipment() {
      try {
        const response = await fetch('http://localhost:8000/equipment', {
          method: 'GET',
          headers: {
            'Accept': 'application/json'
          }
        });
        if (!response.ok) {
          throw new Error('Failed to fetch equipment');
        }
        const data = await response.json();
        this.equipment = data; // Assign fetched equipment data to the 'equipment' array
      } catch (error) {
        console.error(error);
      }
    },
    openEditDialog(equipment) {
      this.selectedEquipment = equipment; // Set the selected equipment
    }
  }
};
</script>

<style scoped>
.selected {
  border: 2px solid blue;
  /* Add styling for selected card */
}
</style>