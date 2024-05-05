import { ref } from 'vue';

// Create reactive variables for loading state and dialog visibility
export const loading = ref(false);
export const open = ref(false);

// Define the useHelpers function
export function useHelpers() {
    // Implementation of the useHelpers function
    return {
        loading,
        open
    };
}
