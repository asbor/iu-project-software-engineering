<template>
    <div>
        <!-- Header -->
        <header>
            <div>
                <h1 class="text-2xl font-semibold">Create a New Reference</h1>
            </div>
        </header>

        <!-- Main section -->
        <main>
            <div v-if="isLoading">
                <Loading :title="isLoadingTitle" />
            </div>
            <div v-if="!isLoading">
                <form @submit.prevent="createReference">
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
                    <!-- Footer -->
                    <footer class="flex justify-end gap-4 mt-8">
                        <Button @click="createReference">Save</Button>
                        <Button @click="cancel">Cancel</Button>
                    </footer>
                </form>
            </div>
        </main>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const reference = ref({
    name: '',
    url: '',
    description: '',
    category: '',
});

const isLoading = ref(false);
const isLoadingTitle = ref('Loading...');

async function createReference() {
    isLoading.value = true;
    isLoadingTitle.value = 'Saving reference...';
    try {
        await $fetch('http://localhost:8000/references', {
            method: 'POST',
            body: reference.value,
        });
        router.push('/references');
    } catch (error) {
        console.error(error);
    } finally {
        isLoading.value = false;
    }
}

function cancel() {
    router.push('/references');
}
</script>
