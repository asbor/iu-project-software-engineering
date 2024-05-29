<script setup>
import { ref, onMounted } from 'vue';

const loading = ref(false);
const style_guidelines = ref([]);
const searchQuery = ref('');
const suggestions = ref([]);
const selectedSuggestionIndex = ref(-1);
const suggestionsDropdown = ref(null);

async function fetchStyleGuidelines() {
    try {
        loading.value = true;
        const response = await fetch('http://localhost:8000/style_guidelines', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        });
        if (!response.ok) {
            throw new Error('Failed to fetch style_guidelines');
        }
        style_guidelines.value = await response.json();
        loading.value = false;
    } catch (error) {
        console.error(error);
    }
}

onMounted(fetchStyleGuidelines);

function searchStyleGuidelines() {
    const query = searchQuery.value.toLowerCase();
    return style_guidelines.value.filter(style => {
        // Filter style_guidelines based on the search query
        return style.category.toLowerCase().includes(query);
    });
}

function updateSuggestions() {
    const query = searchQuery.value.toLowerCase();
    const filteredSuggestions = style_guidelines.value.filter(style => {
        // Filter style_guidelines based on the search query
        return style.category.toLowerCase().includes(query);
    }).map(style => style.category);
    suggestions.value = filteredSuggestions.slice(0, 3); // Limit to top 3 suggestions
}

function selectSuggestion(suggestion) {
    searchQuery.value = suggestion;
    selectedSuggestionIndex.value = -1;
    suggestions.value = []; // Clear suggestions after selecting
}

function closeSuggestionsOnEsc(event) {
    if (event.key === 'Escape' && suggestions.value.length > 0) {
        suggestions.value = [];
    }
}

function handleArrowKeys(event) {
    if (event.key === 'ArrowUp' && selectedSuggestionIndex.value > 0) {
        selectedSuggestionIndex.value--;
    } else if (event.key === 'ArrowDown' && selectedSuggestionIndex.value < suggestions.value.length - 1) {
        selectedSuggestionIndex.value++;
    }
}

function handleEnterKey() {
    if (selectedSuggestionIndex.value !== -1) {
        selectSuggestion(suggestions.value[selectedSuggestionIndex.value]);
    }
}

onMounted(() => {
    document.addEventListener('keydown', closeSuggestionsOnEsc);
});

onUnmounted(() => {
    document.removeEventListener('keydown', closeSuggestionsOnEsc);
});
</script>

<style>
.selected {
    background-color: #f0f0f0;
}
</style>

<template>
    <div class="grid w-full gap-4">
        <header class="flex items-start justify-between">
            <div class="grow">
                <h1>Beer Style Guidelines</h1>
            </div>
            <ProductNewDialog />
            <ButtonsScriptTrigger />
        </header>
        <main class="grid w-full gap-4">
            <div>
                <input type="text" v-model="searchQuery" @input="updateSuggestions"
                    @keydown.enter.prevent="handleEnterKey" @keydown="handleArrowKeys"
                    placeholder="Search for style guidelines..."
                    class="w-full p-2 border border-neutral-200 rounded bg-neutral-200" />
                <ul ref="suggestionsDropdown" v-if="suggestions.length > 0"
                    class="absolute bg-white border border-gray-300 rounded mt-1 w-full">
                    <li v-for="(suggestion, index) in suggestions" :key="index"
                        :class="{ 'selected': index === selectedSuggestionIndex }" @click="selectSuggestion(suggestion)"
                        @mouseenter="selectedSuggestionIndex = index">
                        {{ suggestion }}
                    </li>
                </ul>
            </div>
            <div class="grid gap-4 lg:grid-cols-2">
                <div v-if="loading">Loading...</div>
                <template v-else>
                    <StyleCard v-for="(style, index) in searchStyleGuidelines()" :key="index" :style="style" />
                </template>
            </div>
        </main>
        <footer>
            <!-- Footer content -->
        </footer>
    </div>
</template>
