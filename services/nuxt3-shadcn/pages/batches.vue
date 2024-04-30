<template>
    <div>
        <h1>Authors</h1>
        <ul>
            <li v-for="author in authors" :key="author.id">
                <strong>Name:</strong> {{ author.name }}<br>
                <strong>Surname:</strong> {{ author.surname }}<br>
                <strong>Created At:</strong> {{ author.created_at }}<br>
                <strong>Updated At:</strong> {{ author.updated_at }}<br>
                <button @click="deleteAuthor(author.id)">Delete</button>
            </li>
        </ul>
        <form @submit.prevent="createAuthor">
            <input type="text" v-model="newAuthorName" placeholder="Name">
            <input type="text" v-model="newAuthorSurname" placeholder="Surname">
            <button type="submit">Add Author</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            authors: [],
            newAuthorName: '',
            newAuthorSurname: ''
        };
    },
    async created() {
        await this.fetchAuthors();
    },
    methods: {
        async fetchAuthors() {
            try {
                const response = await fetch('http://localhost:8000/authors', {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                if (!response.ok) {
                    throw new Error('Failed to fetch authors');
                }
                const data = await response.json();
                this.authors = data;
            } catch (error) {
                console.error(error);
            }
        },
        async createAuthor() {
            try {
                const response = await fetch('http://localhost:8000/authors', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        // autoincrement uuid
                        // id format: 558687de-d967-464e-84d7-c2bd89371586
                        id: Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15),
                        name: this.newAuthorName,
                        surname: this.newAuthorSurname,
                        created_at: new Date().toISOString(), // format: 2024-04-29T13:00:00.158Z
                        updated_at: new Date().toISOString() // format: 2024-04-29T13:00:00.158Z

                    })
                });
                if (!response.ok) {
                    throw new Error('Failed to create author');
                }
                await this.fetchAuthors();
                this.newAuthorName = '';
                this.newAuthorSurname = '';
            } catch (error) {
                console.error(error);
            }
        },
        async deleteAuthor(authorId) {
            try {
                const response = await fetch(`http://localhost:8000/authors/${authorId}`, {
                    method: 'DELETE'
                });
                if (!response.ok) {
                    throw new Error('Failed to delete author');
                }
                await this.fetchAuthors();
            } catch (error) {
                console.error(error);
            }
        }
    }
};
</script>
