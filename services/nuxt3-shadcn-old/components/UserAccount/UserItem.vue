<script setup>
const loading = ref(false)
const name = "Asbjorn Bordoy"
const occupation = "Software Engineer"
</script>

<template>
  <div class="p-4">
    <div
      class="flex items-center gap-2 cursor-pointer hover:bg-neutral-50 rounded p-2 border rounded hover:text-blue-500">
      <div class="bg-blue-300 h-10 w-10 rounded-full flex items-center justify-center font-bold text-white">{{
        name[0] }}</div>
      <div>
        <h2 class="m-0 text-sm font-bold leadning-1">{{ name }}</h2>
        <p class="m-0 text-xs">{{ occupation }}</p>
      </div>
    </div>
  </div>
</template>