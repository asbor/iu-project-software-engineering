// ExampleComponent.vue
<template>
    <div>
        <h1>Notes:</h1>
        <ul>
            <li v-for="note in notes" :key="note.id">
                {{ note.title }} - {{ note.content }}
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            notes: []
        };
    },
    mounted() {
        this.fetchNotes();
    },
    methods: {
        async fetchNotes() {
            try {
                const token = 'Bearer YOUR_ACCESS_TOKEN'; // Replace with your actual access token
                const config = {
                    headers: {
                        Authorization: token
                    }
                };
                const response = await axios.get('http://localhost:5000/notes', config);
                this.notes = response.data;
            } catch (error) {
                console.error('Error fetching notes:', error);
            }
        }
    }
}
</script>
