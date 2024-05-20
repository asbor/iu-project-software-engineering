<template>
  <div>
    <!-- Header -->
    <header>
      <div>
        <h1 class="text-2xl font-semibold">Create a new recipe item</h1>
      </div>
    </header>

    <!-- Main section -->
    <main>
      <div v-if="isLoading">
        <Loading :title="isLoadingTitle" />
      </div>
      <div v-if="!isLoading">



        <form @submit.prevent="saveRecipe">
          <!-- Input fields 
        name (str): The name of the recipe.
        type (str): The type or style of the recipe.
        brewer (str): The name of the primary brewer.
        asst_brewer (str): The name of the assistant brewer.
        batch_size (int): The size of the batch in liters.
        boil_size (int): The size of the boil in liters.
        boil_time (int): The duration of the boil in minutes.
        efficiency (int): The brewing efficiency as a percentage.
        hop (relationship): Relationship to the Hop table.
        fermentable (relationship): Relationship to the fermentable table.
        # misc (relationship): Relationship to the Misc table.
        yeast (relationship): Relationship to the Yeast table.
        #water (relationship): Relationship to the Water table.
        style (relationship): Relationship to the Style table.
        equipment (relationship): Relationship to the Equipment table.
        mash (str): Details about the mashing process.
        notes (str): General notes about the recipe.
        taste_notes (str): Notes about the taste of the final product.
        taste_rating (int): A rating for the taste of the final product.
        og (int): Original gravity of the beer.
        fg (int): Final gravity of the beer.
        carbonation (int): Level of carbonation.
        fermentation_stages (int): Number of fermentation stages.
        primary_age (int): Age of the beer during primary fermentation.
        primary_temp (int): Temperature during primary fermentation.
        secondary_age (int): Age of the beer during secondary fermentation.
        secondary_temp (int): Temperature during secondary fermentation.
        tertiary_age (int): Age of the beer during tertiary fermentation.
        age (int): Age of the beer in days.
        age_temp (int): Temperature during aging.
        carbonation_used (str): Details about carbonation used.
        date (Date): The date when the recipe was created.
        est_og (int): Estimated original gravity.
        est_fg (int): Estimated final gravity.
        est_color (int): Estimated color of the beer.
        ibu (int): International Bitterness Units.
        ibu_method (str): Method used to calculate IBU.
        est_abv (int): Estimated alcohol by volume.
        abv (int): Actual alcohol by volume.
        actual_efficiency (int): Actual brewing efficiency.
        calories (int): Estimated calories per serving.
        display_batch_size (str): Formatted batch size.
        display_boil_size (str): Formatted boil size.
        display_og (str): Formatted original gravity.
        display_fg (str): Formatted final gravity.
        display_primary_temp (str): Formatted primary fermentation temperature.
        display_secondary_temp (str): Formatted secondary fermentation temperature.
        display_tertiary_temp (str): Formatted tertiary fermentation temperature.
          -->
          <div>
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="recipe.name" required placeholder="Optional"
              class="border-2 border-gray-300 rounded-lg p-2 w-full">
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
/*
  Attributes:

*/

import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      recipe: {
        name: '',
        type: '',
        brewer: '',
        asst_brewer: '',

        batch_size: 0,
        boil_size: 0,
        boil_time: 0,
        efficiency: 0,

        // Relationships
        hops: [
          {
            name: '',
            alpha: 0,
            amount: 0,
            use: '',
            time: 0,
            notes: '',
          },
        ],
        fermentables: [], // List of fermentable objects (relationship)
        //misc: [],         // List of misc objects (relationship)
        //yeass: [],        // List of yeast objects (relationship)
        style: {},        // Style object (relationship)
        //equipment: {},    // Equipment object (relationship)
        mash: '',
        notes: '',
        taste_notes: '',
        taste_rating: 0,
        og: 0,
        fg: 0,
        carbonation: 0,
        fermentation_stages: 0,
        primary_age: 0,

      },
      isLoading: false,
      isLoadingTitle: 'Loading...',
    };
  },
  methods: {
    saveRecipe() {
      this.isLoading = true;
      this.isLoadingTitle = 'Saving...';
      // Save the recipe profile
      console.log(this.recipe);
      axios.post('http://localhost:8000/recipe/', this.recipe)
        .then(res => {
          console.log(res, 'res');
          // Redirect to the previous page or perform any other action after saving
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
    },
  },
};
</script>
