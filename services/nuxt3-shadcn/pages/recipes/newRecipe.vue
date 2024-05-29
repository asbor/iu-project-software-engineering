<template>
  <div>
    <!-- Header -->
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Create a New Recipe</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <div v-if="isLoading">
        <Loading :title="isLoadingTitle" />
      </div>
      <div v-if="!isLoading">
        <form @submit.prevent="saveRecipe">
          <!-- Three columns -->
          <div class="grid grid-cols-3 gap-4">
            <RecipeBlock class="border-2 p-4">
              <div>
                <label for="name">Name:</label>
                <input type="text" id="name" v-model="recipe.name" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="brewer">Brewer:</label>
                <input type="text" id="brewer" v-model="recipe.brewer" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="type">Type:</label>
                <input type="text" id="type" v-model="recipe.type" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </RecipeBlock>

            <EquipmentBlock class="border-2 p-4">
              <div>
                <label for="batch_size">Batch Size:</label>
                <input type="number" id="batch_size" v-model="recipe.batch_size" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="boil_size">Boil Size:</label>
                <input type="number" id="boil_size" v-model="recipe.boil_size" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="boil_time">Boil Time:</label>
                <input type="number" id="boil_time" v-model="recipe.boil_time" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="efficiency">Efficiency:</label>
                <input type="number" id="efficiency" v-model="recipe.efficiency" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </EquipmentBlock>

            <StyleBlock class="border-2 p-4">
              <div>
                <label for="abv">ABV:</label>
                <input type="number" id="abv" v-model="recipe.abv" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="og">OG:</label>
                <input type="number" id="og" v-model="recipe.og" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="fg">FG:</label>
                <input type="number" id="fg" v-model="recipe.fg" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="ibu">IBU:</label>
                <input type="number" id="ibu" v-model="recipe.ibu" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
              <div>
                <label for="est_color">EBC:</label>
                <input type="number" id="est_color" v-model="recipe.est_color" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </StyleBlock>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <FermentablesBlock class="border-2 p-4">
              <div>
                <label for="fermentables">Fermentables:</label>
                <div v-for="(fermentable, index) in recipe.fermentables" :key="index">
                  <input type="text" v-model="fermentable.name" required placeholder="Optional"
                    class="border-2 border-gray-300 rounded-lg p-2 w-full">
                </div>
              </div>
            </FermentablesBlock>

            <HopsBlock class="border-2 p-4">
              <div>
                <label for="hops">Hops:</label>
                <div v-for="(hop, index) in recipe.hops" :key="index">
                  <input type="text" v-model="hop.name" required placeholder="Optional"
                    class="border-2 border-gray-300 rounded-lg p-2 w-full">
                </div>
              </div>
            </HopsBlock>

            <MiscsBlock class="border-2 p-4">
              <div>
                <label for="miscs">Miscs:</label>
                <div v-for="(misc, index) in recipe.miscs" :key="index">
                  <input type="text" v-model="misc.name" required placeholder="Optional"
                    class="border-2 border-gray-300 rounded-lg p-2 w-full">
                </div>
              </div>
            </MiscsBlock>

            <YeastBlock class="border-2 p-4">
              <div>
                <label for="yeasts">Yeasts:</label>
                <div v-for="(yeast, index) in recipe.yeasts" :key="index">
                  <input type="text" v-model="yeast.name" required placeholder="Optional"
                    class="border-2 border-gray-300 rounded-lg p-2 w-full">
                </div>
              </div>
            </YeastBlock>

            <MashBlock class="border-2 p-4">
              <div>
                <label for="mash">Mash:</label>
                <input type="text" id="mash" v-model="recipe.mash" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </MashBlock>

            <FermentationBlock class="border-2 p-4">
              <div>
                <label for="fermentation">Fermentation:</label>
                <input type="text" id="fermentation" v-model="recipe.fermentation" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </FermentationBlock>
          </div>

          <div class="grid grid-cols-1 gap-4">
            <WaterBlock class="border-2 p-4">
              <div>
                <label for="water">Water:</label>
                <input type="text" id="water" v-model="recipe.water" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full">
              </div>
            </WaterBlock>

            <NotesBlock class="border-2 p-4">
              <div>
                <label for="notes">Notes:</label>
                <textarea id="notes" v-model="recipe.notes" required placeholder="Optional"
                  class="border-2 border-gray-300 rounded-lg p-2 w-full"></textarea>
              </div>
            </NotesBlock>
          </div>
        </form>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-end gap-4 mt-8">
      <Button @click="saveRecipe">Save</Button>
      <Button @click="cancel">Cancel</Button>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  data() {
    return {
      recipe: {
        name: '',
        version: 0,
        type: '',
        brewer: '',
        asst_brewer: '',
        batch_size: 0,
        boil_size: 0,
        boil_time: 0,
        efficiency: 0,
        notes: '',
        taste_notes: '',
        taste_rating: 0,
        og: 0,
        fg: 0,
        fermentation_stages: 0,
        primary_age: 0,
        primary_temp: 0,
        secondary_age: 0,
        secondary_temp: 0,
        tertiary_age: 0,
        age: 0,
        age_temp: 0,
        carbonation_used: '',
        carbonation_date: '',
        est_og: 0,
        est_fg: 0,
        est_color: 0,
        ibu: 0,
        ibu_method: '',
        est_abv: 0,
        abv: 0,
        actual_efficiency: 0,
        calories: 0,
        display_batch_size: '',
        display_boil_size: '',
        display_og: '',
        display_fg: '',
        display_primary_temp: '',
        display_secondary_temp: '',
        display_tertiary_temp: '',
        display_age_temp: '',
        hops: [],
        fermentables: [],
        miscs: [],
        yeasts: [],
      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  methods: {
    async saveRecipe() {
      this.isLoading = true;
      this.isLoadingTitle = 'Saving...';
      try {
        await $fetch('http://localhost:8000/recipes', {
          method: 'POST',
          body: this.recipe,
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
