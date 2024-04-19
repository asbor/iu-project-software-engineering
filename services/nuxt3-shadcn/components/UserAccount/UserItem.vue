<script setup>
const loading = ref(false)
const name = "Asbjorn Bordoy"
const occupation = "Software Engineer"
</script>

<template>
  <div class="p-4">
    <div class="flex items-center gap-2 text-black cursor-pointer hover:bg-neutral-50 rounded p-2 border rounded">
      <div class="bg-blue-300 h-10 w-10 rounded-full flex items-center justify-center font-bold text-white">{{
        name[0] }}</div>
      <div>
        <p class="m-0 text-sm font-bold text-black leadning-1">{{ name }}</p>
        <p class="m-0 text-xs">{{ occupation }}</p>
      </div>
    </div>
  </div>
</template>