<template>
    <div>
        <!-- Header -->
        <header>
            <div>
                <h1 class="text-2xl font-semibold">Create a new yeast item</h1>
            </div>
        </header>

        <!-- Main section -->
        <main>
            <div v-if="isLoading">
                <Loading :title="isLoadingTitle" />
            </div>
            <div v-if="!isLoading">
                <form @submit.prevent="saveYeast">
                    <div>
                        <label for="name">Name:</label>
                        <input type="text" id="name" v-model="yeast.name" required placeholder="Optional"
                            class="border-2 border-gray-300 rounded-lg p-2 w-full">
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="type">Type:</label>
                            <input type="text" id="type" v-model="yeast.type" required placeholder="Optional"
                                class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="form">Form:</label>
                            <input type="text" id="form" v-model="yeast.form" required placeholder="Optional"
                                class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="laboratory">Laboratory:</label>
                            <input type="text" id="laboratory" v-model="yeast.laboratory" required
                                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="product_id">Product ID:</label>
                            <input type="text" id="product_id" v-model="yeast.product_id" required
                                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="min_temperature">Min Temperature:</label>
                            <input type="number" id="min_temperature" v-model="yeast.min_temperature" required
                                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="max_temperature">Max Temperature:</label>
                            <input type="number" id="max_temperature" v-model="yeast.max_temperature" required
                                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="flocculation">Flocculation:</label>
                            <input type="text" id="flocculation" v-model="yeast.flocculation" required
                                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="attenuation">Attenuation:</label>
                            <input type="number" id="attenuation" v-model="yeast.attenuation" required
                                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="max_reuse">Max Reuse:</label>
                            <input type="number" id="max_reuse" v-model="yeast.max_reuse" required
                                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="amount">Amount:</label>
                            <input type="number" id="amount" v-model="yeast.amount" required placeholder="Optional"
                                class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="amount_is_weight">Amount is Weight:</label>
                            <input type="checkbox" id="amount_is_weight" v-model="yeast.amount_is_weight"
                                class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="times_cultured">Times Cultured:</label>
                            <input type="number" id="times_cultured" v-model="yeast.times_cultured" required
                                placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                        <div>
                            <label for="add_to_secondary">Add to Secondary:</label>
                            <input type="checkbox" id="add_to_secondary" v-model="yeast.add_to_secondary"
                                class="border-2 border-gray-300 rounded-lg p-2 w-full">
                        </div>
                    </div>
                    <div>
                        <label for="notes">Notes:</label>
                        <textarea id="notes" v-model="yeast.notes"
                            class="w-full border-2 border-gray-300 rounded-lg p-2"></textarea>
                    </div>
                    <div>
                        <label for="best_for">Best For:</label>
                        <input type="text" id="best_for" v-model="yeast.best_for" required placeholder="Optional"
                            class="border-2 border-gray-300 rounded-lg p-2 w-full">
                    </div>
                    <div>
                        <label for="display_amount">Display Amount:</label>
                        <input type="text" id="display_amount" v-model="yeast.display_amount" required
                            placeholder="Optional" class="border-2 border-gray-300 rounded-lg p-2 w-full">
                    </div>
                    <div>
                        <label for="inventory">Inventory:</label>
                        <input type="number" id="inventory" v-model="yeast.inventory" required placeholder="Optional"
                            class="border-2 border-gray-300 rounded-lg p-2 w-full">
                    </div>
                </form>
            </div>
        </main>

        <!-- Footer -->
        <footer class="flex justify-end gap-4 mt-8">
            <Button @click="saveYeast">Save</Button>
            <Button @click="cancel">Cancel</Button>
        </footer>
    </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
    data() {
        return {
            yeast: {
                name: '',
                type: '',
                form: '',
                laboratory: '',
                product_id: '',
                min_temperature: 0,
                max_temperature: 0,
                flocculation: '',
                attenuation: 0,
                notes: '',
                best_for: '',
                max_reuse: 0,
                amount: 0,
                amount_is_weight: false,
                inventory: 0,
                display_amount: '',
                times_cultured: 0,
                add_to_secondary: false,
            },
            isLoading: false,
            isLoadingTitle: 'Loading...',
        };
    },
    methods: {
        async saveYeast() {
            this.isLoading = true;
            this.isLoadingTitle = 'Saving...';
            try {
                await $fetch('http://localhost:8000/inventory/yeasts', {
                    method: 'POST',
                    body: this.yeast,
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
        },
    },
};
</script>
