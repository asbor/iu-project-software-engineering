<template>
    <section>
        <form @submit.prevent="submit">
            <div class="mb-3">
                <label for="username" class="form-label">Username:</label>
                <input type="text" name="username" v-model="form.username" class="form-control" />
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" name="password" v-model="form.password" class="form-control" />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </section>
</template>

<script>
export default {
    data() {
        return {
            form: {
                username: '',
                password: '',
            }
        };
    },
    methods: {
        async submit() {
            // Implement your login logic here
            // Example: make an API request to authenticate the user
            try {
                // Replace this with your actual login logic
                const response = await fetch('http://your-backend-url/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.form),
                });
                if (response.ok) {
                    // Redirect to the dashboard or home page upon successful login
                    this.$router.push('/dashboard');
                } else {
                    // Handle invalid credentials or other errors
                    console.error('Login failed');
                }
            } catch (error) {
                console.error('Error during login:', error);
            }
        }
    }
};
</script>