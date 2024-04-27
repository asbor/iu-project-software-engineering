<script setup>
const runtimeConfigs = useRuntimeConfig();
const page = ref(1);

const { data, pending } = await useFetch(() => `${runtimeConfigs.public.API_URL}/users?page=${page.value}`, {
    key: `userlist-${page.value}`,
}
</script>

<template>
    <div>Hello</div>
</template>