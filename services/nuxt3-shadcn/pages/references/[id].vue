<template>
    <div>
        <!-- Header -->
        <header>
            <div>
                <h1 class="text-2xl font-semibold">Edit Reference</h1>
            </div>
        </header>

        <!-- Main section -->
        <main>
            <div v-if="isLoading">
                <Loading :title="isLoadingTitle" />
            </div>
            <div v-if="!isLoading">
                <form @submit.prevent="updateReference">
                    <!-- Form fields -->
                    <div class="grid grid-cols-1 gap-4">
                        <div class="border-2 p-4">
                            <div>
                                <label for="name">Name:</label>
                                <input type="text" id="name" v-model="reference.name" required placeholder="Name"
                                    class="border-2 border-gray-300 rounded-lg p-2 w-full">
                            </div>
                            <div>
                                <label for="url">URL:</label>
                                <input type="url" id="url" v-model="reference.url" required
                                    placeholder="https://example.com"
                                    class="border-2 border-gray-300 rounded-lg p-2 w-full">
                            </div>
                            <div>
                                <label for="description">Description:</label>
                                <textarea id="description" v-model="reference.description" placeholder="Description"
                                    class="border-2 border-gray-300 rounded-lg p-2 w-full"></textarea>
                            </div>
                            <div>
                                <label for="category">Category:</label>
                                <input type="text" id="category" v-model="reference.category" placeholder="Category"
                                    class="border-2 border-gray-300 rounded-lg p-2 w-full">
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </main>

        <!-- Footer -->
        <footer class="flex justify-end gap-4 mt-8">
            <Button @click="updateReference">Save</Button>
            <Button @click="cancel">Cancel</Button>
        </footer>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const route = useRoute();

const reference = ref({
    name: '',
    url: '',
    description: '',
    category: '',
});

const isLoading = ref(false);
const isLoadingTitle = ref('Loading...');

async function getReferenceProfile(id: number) {
    isLoading.value = true;
    isLoadingTitle.value = 'Loading reference...';
    try {
        const response = await axios.get(`http://localhost:8000/references/${id}`);
        reference.value = response.data;
    } catch (error) {
        console.error(error);
    } finally {
        isLoading.value = false;
    }
}

async function updateReference() {
    isLoading.value = true;
    isLoadingTitle.value = 'Updating reference...';
    try {
        await axios.put(`http://localhost:8000/references/${reference.value.id}`, reference.value);
        router.back();
    } catch (error) {
        console.error(error);
    } finally {
        isLoading.value = false;
    }
}

function cancel() {
    router.back();
}

onMounted(() => {
    const id = route.params.id;
    getReferenceProfile(Number(id));
});
</script>