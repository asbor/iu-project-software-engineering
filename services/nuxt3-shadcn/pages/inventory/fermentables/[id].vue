<script>
/*
Fermentable creation schema

Attributes:
    id : The unique identifier for the fermentable.
    name (str): The name of the fermentable.
    amount (int): The amount of the fermentable in kilograms.
    cost_per_unit (float): The cost per unit in Euros.
    supplier (str): The supplier of the fermentable.
    origin (str): The origin of the fermentable.
    type (str): The type of the fermentable.
    color (int): The color of the fermentable in EBC.
    potential (int): The potential of the fermentable in PPG (Points Per Gallon).
    yield_ (float): The yield of the fermentable as a percentage.
    manufacturing_date (str): The manufacturing date of the fermentable.
    expiry_date (str): The expiry date of the fermentable.
    lot_number (str): The lot number of the fermentable.
    exclude_from_total (bool): Indicates whether to exclude the fermentable from the total.
    not_fermentable (bool): Indicates whether the fermentable is not fermentable.
    notes (str): Additional notes about the fermentable.
    description (str): Description of the fermentable.
    substitutes (str): Substitutes for the fermentable.
    used_in (str): Where the fermentable is used.
*/
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      fermentable: {
        id: '',
        name: '',
        amount: 0,
        cost_per_unit: 0,
        supplier: '',
        origin: '',
        type: '',
        color: 0,
        potential: 0,
        yield_: 0,
        manufacturing_date: '',
        expiry_date: '',
        lot_number: '',
        exclude_from_total: false,
        not_fermentable: false,
        notes: '',
        description: '',
        substitutes: '',
        used_in: '',
      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  mounted() {
    // Get the id of the fermentable profile
    this.id = this.$route.params.id;
    this.getFermentableProfile(this.id);
  },
  methods: {
    getFermentableProfile(id) {
      this.isLoading = true;
      this.isLoadingTitle = 'Loading fermentable...';
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
      this.isLoading = false;
    },
    updateFermentable() {
      this.isLoading = true;
      this.isLoadingTitle = 'Updating fermentable...';
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
        <form @submit.prevent="updateFermentable">
          <div>
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="fermentable.name" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
          </div>
          <InventoryAmount>
            <div class="flex items-center justify-between gap-2 mt-4 mb-2">
              <label for="amount">Inventory Amount</label>
              <label for="amount_EngUnit">kg</label>
            </div>
            <div>
              <input type="number" id="amount" v-model="fermentable.amount" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </InventoryAmount>
          <CostPerUnit>
            <div class="flex items center justify-between gap-2 mt-4 mb-2">
              <label for="cost">Cost per unit</label>
              <label for="cost_EngUnit">EUR</label>
            </div>
            <div>
              <input type="number" id="cost" v-model="fermentable.cost_per_unit" required placeholder="Optional"
                class=" border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </CostPerUnit>

          <div class="grid grid-cols-3 gap-4">
            <Supplier>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="supplier">Supplier</label>
              </div>
              <div>
                <input type="text" id="supplier" v-model="fermentable.supplier" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Supplier>
            <Origin>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="origin">Origin</label>
              </div>
              <div>
                <input type="text" id="origin" v-model="fermentable.origin" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Origin>
            <Type>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="type">Type</label>
              </div>
              <div>
                <input type="text" id="type" v-model="fermentable.type" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Type>
            <Color>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="color">Color</label>
                <label for="color_EngUnit">EBC</label>
              </div>
              <div>
                <input type="number" id="color" v-model="fermentable.color" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Color>
            <Potential>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="potential">Potential</label>
                <label for="potential_EngUnit">PPG</label>
              </div>
              <div>
                <input type="number" id="potential" v-model="fermentable.potential" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Potential>
            <Yield>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="yield">Yield</label>
                <label for="yield_EngUnit">%</label>
              </div>
              <div>
                <input type="number" id="yield" v-model="fermentable.yield" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </Yield>
            <ManufactureringDate>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="manufacturering_date">Manufacturering Date</label>
              </div>
              <div>
                <input type="date" id="manufacturering_date" v-model="fermentable.manufacturering_date" required
                  placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </ManufactureringDate>
            <ExpiryDate>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="expiry_date">Expiry Date</label>
              </div>
              <div>
                <input type="date" id="expiry_date" v-model="fermentable.expiry_date" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </ExpiryDate>
          </div>
          <LotNumber>
            <div class="flex items center justify-between gap-2 mt-4 mb-2">
              <label for="lot_number">Lot Number</label>
            </div>
            <div>
              <input type="text" id="lot_number" v-model="fermentable.lot_number" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
            </div>
          </LotNumber>
          <div class="grid grid-cols-2 gap-4">
            <ExclFromTotal class="flex items center gap-2 mt-4 mb-2">
              <div>
                <input type="checkbox" id="excl_from_total" v-model="fermentable.excl_from_total" required
                  placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="excl_from_total">Exclude from total</label>
              </div>
            </ExclFromTotal>
            <NotFermentable class="flex items center gap-2 mt-4 mb-2">
              <div>
                <input type="checkbox" id="not_fermentable" v-model="fermentable.not_fermentable" required
                  placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="not_fermentable">Not fermentable</label>
              </div>
            </NotFermentable>
          </div>
          <Notes>
            <div class="flex items center justify-between gap-2 mt-4 mb-2">
              <label for="notes">Notes:</label>
            </div>
            <div class="flex fill-current w-full">
              <textarea id="notes" v-model="fermentable.notes"
                class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
            </div>
          </Notes>
          <Details>
            <Description>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="description">Description:</label>
              </div>
              <div class="flex fill-current w-full">
                <textarea id="description" v-model="fermentable.description"
                  class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
              </div>
            </Description>
            <Substitutes>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="substitutes">Substitutes:</label>
              </div>
              <div class="flex fill-current w-full">
                <textarea id="substitutes" v-model="fermentable.substitutes"
                  class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
              </div>
            </Substitutes>
            <UsedIn>
              <div class="flex items center justify-between gap-2 mt-4 mb-2">
                <label for="used_in">Used in:</label>
              </div>
              <div class="flex fill-current w-full">
                <textarea id="used_in" v-model="fermentable.used_in"
                  class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
              </div>
            </UsedIn>
          </Details>


        </form>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="updateFermentable">Save</Button>
      <Button @click="cancel">Cancel</Button>
    </footer>
  </div>
</template>