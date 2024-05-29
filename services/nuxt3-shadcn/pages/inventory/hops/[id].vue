<template>
  <div>
    <!-- Header -->
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Edit Hop Item</h1>
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
          <InventoryAmount>
            <div class="flex items-center justify-between gap-2 mt-4 mb-2">
              <label for="amount">Inventory Amount</label>
              <label for="amount_EngUnit">kg</label>
            </div>
            <div>
              <input type="number" id="amount" v-model="hop.amount" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </InventoryAmount>
          <CostPerUnit>
            <div class="flex items-center justify-between gap-2 mt-4 mb-2">
              <label for="cost">Cost per unit</label>
              <label for="cost_EngUnit">EUR</label>
            </div>
            <div>
              <input type="number" id="cost_per_unit" v-model="hop.cost_per_unit" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </CostPerUnit>

          <div class="grid grid-cols-3 gap-4">
            <Supplier>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="supplier">Supplier</label>
              </div>
              <div>
                <input type="text" id="supplier" v-model="hop.supplier" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Supplier>
            <Origin>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="origin">Origin</label>
              </div>
              <div>
                <input type="text" id="origin" v-model="hop.origin" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Origin>
            <Type>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="type">Type</label>
              </div>
              <div>
                <input type="text" id="type" v-model="hop.type" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Type>
            <Color>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="color">Color</label>
                <label for="color_EngUnit">EBC</label>
              </div>
              <div>
                <input type="number" id="color" v-model="hop.color" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Color>
            <Potential>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="potential">Potential</label>
                <label for="potential_EngUnit">PPG</label>
              </div>
              <div>
                <input type="number" id="potential" v-model="hop.potential" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Potential>
            <Yield>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="yield">Yield</label>
                <label for="yield_EngUnit">%</label>
              </div>
              <div>
                <input type="number" id="yield_" v-model="hop.yield_" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Yield>
            <ManufacturingDate>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="manufacturing_date">Manufacturing Date</label>
              </div>
              <div>
                <input type="date" id="manufacturing_date" v-model="hop.manufacturing_date" required
                  placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </ManufacturingDate>
            <ExpiryDate>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="expiry_date">Expiry Date</label>
              </div>
              <div>
                <input type="date" id="expiry_date" v-model="hop.expiry_date" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </ExpiryDate>
          </div>
          <LotNumber>
            <div class="flex items-center justify-between gap-2 mt-4 mb-2">
              <label for="lot_number">Lot Number</label>
            </div>
            <div>
              <input type="text" id="lot_number" v-model="hop.lot_number" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </LotNumber>
          <div class="grid grid-cols-2 gap-4">
            <ExclFromTotal class="flex items-center gap-2 mt-4 mb-2">
              <div>
                <input type="checkbox" id="excl_from_total" v-model="hop.excl_from_total" required
                  placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="excl_from_total">Exclude from total</label>
              </div>
            </ExclFromTotal>
            <NotHop class="flex items-center gap-2 mt-4 mb-2">
              <div>
                <input type="checkbox" id="not_hop" v-model="hop.not_hop" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="not_hop">Not hop</label>
              </div>
            </NotHop>
          </div>
          <Notes>
            <div class="flex items-center justify-between gap-2 mt-4 mb-2">
              <label for="notes">Notes:</label>
            </div>
            <div class="flex fill-current w-full">
              <textarea id="notes" v-model="hop.notes"
                class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
            </div>
          </Notes>
          <Details>
            <Description>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="description">Description:</label>
              </div>
              <div class="flex fill-current w-full">
                <textarea id="description" v-model="hop.description"
                  class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
              </div>
            </Description>
            <Substitutes>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="substitutes">Substitutes:</label>
              </div>
              <div class="flex fill-current w-full">
                <textarea id="substitutes" v-model="hop.substitutes"
                  class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
              </div>
            </Substitutes>
            <UsedIn>
              <div class="flex items-center justify-between gap-2 mt-4 mb-2">
                <label for="used_in">Used in:</label>
              </div>
              <div class="flex fill-current w-full">
                <textarea id="used_in" v-model="hop.used_in"
                  class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
              </div>
            </UsedIn>
          </Details>
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

<script>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';

export default {
  data() {
    return {
      hop: {
        name: '',
        amount: 0,
        cost_per_unit: 0,
        supplier: '',
        origin: '',
        type: '',
        color: 0,
        potential: 0,
        yield_: 0,
        manufacturing_date: "2024-01-01",
        expiry_date: "2024-01-01",
        lot_number: '',
        exclude_from_total: false,
        not_hop: false,
        notes: '',
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
    await this.getHopProfile(this.id);
  },
  methods: {
    async getHopProfile(id) {
      this.isLoading = true;
      this.isLoadingTitle = 'Loading hop...';
      try {
        const data = await $fetch(`http://localhost:8000/inventory/hops/${id}`);
        this.hop = data;
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async updateHop() {
      this.isLoading = true;
      this.isLoadingTitle = 'Updating hop...';
      try {
        await $fetch(`http://localhost:8000/inventory/hops/${this.id}`, {
          method: 'PUT',
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
    }
  }
};
</script>
