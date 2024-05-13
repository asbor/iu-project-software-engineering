<template>
    <div class="p-2">
        <div class="flex items-center gap-2">
            <div class="indicator"
                :class="{ 'connected': isConnectedToDatabase, 'disconnected': !isConnectedToDatabase }">
            </div>
            <span>{{ isConnectedToDatabase ? 'Connected' : 'Disconnected' }}</span>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'; // Import the ref function from Vue

const isConnectedToDatabase = ref(false); // Define a reactive boolean property

// Define a method to check the database connection status
const checkDatabaseConnection = () => {
    // make an API request to check the database connection status

    fetch('http://localhost:8000/style', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    })
        .then(response => {
            if (response.ok) {
                isConnectedToDatabase.value = true;
            } else {
                isConnectedToDatabase.value = false;
            }
        })
        .catch(error => {
            console.error(error);
            isConnectedToDatabase.value = false;
        });


}

// Call the method to check the database connection status periodically or on demand
checkDatabaseConnection();

</script>


<style scoped>
/* Define styling for the indicator */
.indicator {
    width: 10px;
    height: 10px;
    border-radius: 50%;
}

/* Define styling for connected state */
.connected {
    background-color: green;
}

/* Define styling for disconnected state */
.disconnected {
    background-color: red;
}
</style>