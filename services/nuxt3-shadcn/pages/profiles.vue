<template>
    <div>
        <h1>Users</h1>
        <ul>
            <li v-for="user in users" :key="user.id">
                <strong>Name:</strong> {{ user.name }}<br>
                <strong>Surname:</strong> {{ user.surname }}<br>
                <strong>Email:</strong> {{ user.email }}<br>
                <strong>Birth Date:</strong> {{ user.birth_date }}<br>
                <strong>Personal Identificator:</strong> {{ user.personal_identificator }}<br>
                <button @click="deleteUser(user.id)">Delete</button>
            </li>
        </ul>
        <form @submit.prevent="createUser">
            <input type="text" v-model="newUserName" placeholder="Name">
            <input type="text" v-model="newUserSurname" placeholder="Surname">
            <input type="text" v-model="newUserEmail" placeholder="Email">
            <input type="text" v-model="newUserBirthDate" placeholder="Birth Date (YYYY-MM-DD)">
            <input type="text" v-model="newUserPersonalIdentificator" placeholder="Personal Identificator">
            <input type="text" v-model="newUserCreatedAt" placeholder="Created At">
            <input type="text" v-model="newUserUpdatedAt" placeholder="Updated At">
            <button type="submit">Add User</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            users: [],
            newUserName: '',
            newUserSurname: '',
            newUserEmail: '',
            newUserBirthDate: '',
            newUserPersonalIdentificator: '',
            newUserCreatedAt: '',
            newUserUpdatedAt: ''

        };
    },
    async created() {
        await this.fetchUsers();
    },
    methods: {
        async fetchUsers() {
            try {
                const response = await fetch('http://localhost:8000/user', {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                if (!response.ok) {
                    throw new Error('Failed to fetch users');
                }
                const data = await response.json();
                this.users = data;
            } catch (error) {
                console.error(error);
            }
        },
        async createUser() {
            try {
                const response = await fetch('http://localhost:8000/user', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: this.newUserName,
                        surname: this.newUserSurname,
                        email: this.newUserEmail,
                        birth_date: this.newUserBirthDate,
                        personal_identificator: this.newUserPersonalIdentificator,
                        created_at: new Date().toISOString(), // format: '2024-04-29T13:00:00.158Z'
                        updated_at: new Date().toISOString() // format: '2024-04-29T13:00:00.158Z'
                    })
                });
                if (!response.ok) {
                    throw new Error('Failed to create user');
                }
                await this.fetchUsers();
                this.newUserName = '';
                this.newUserSurname = '';
                this.newUserEmail = '';
                this.newUserBirthDate = '';
                this.newUserPersonalIdentificator = '';
                this.newUserCreatedAt = '';
                this.newUserUpdatedAt = '';
            } catch (error) {
                console.error(error);
            }
        },
        async deleteUser(userId) {
            try {
                const response = await fetch(`http://localhost:8000/user/${userId}`, {
                    method: 'DELETE'
                });
                if (!response.ok) {
                    throw new Error('Failed to delete user');
                }
                await this.fetchUsers();
            } catch (error) {
                console.error(error);
            }
        }
    }
};
</script>
