<script setup lang="ts">
import { ref } from 'vue';
import { useHelpers } from '../composables/helpers'; // Adjust the import path as needed

const { loading, open } = useHelpers();
let mode = 'create'; // Initialize mode as 'create' by default


const formData = ref({
  username: '',
  password: ''
});

const createNewUser = async () => {
  try {
    loading.value = true;
    const url = mode === 'create' ? 'http://localhost:8000/user' : `http://localhost:8000/user/${formData.value.id}`;
    const method = mode === 'create' ? 'POST' : 'PUT';
    const response = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(formData.value),
    });
    if (!response.ok) {
      throw new Error(mode === 'create' ? 'Failed to create user' : 'Failed to save user');
    }
    console.log(mode === 'create' ? 'User created successfully' : 'User saved successfully');
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
    open.value = false;
  }
}
</script>

<template>
  <AlertDialog :open="open">
    <Button @click="open = true">Add a new User</Button>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Create a new User</AlertDialogTitle>
        <Input v-model="formData.username" placeholder="User name" />
        <Input v-model="formData.password" type="password" placeholder="Password" />
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
        <AlertDialogAction @click="createNewUser()">Create</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
