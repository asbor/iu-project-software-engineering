<script setup>
import Button from '../ui/button/Button.vue';

const items = ref([
  // Dashboard
  { title: "Dashboard", path: "/", icon: "ri:dashboard-line" },
  // Beer brewing recipes
  { title: "Recipes", path: "/recipes", icon: "lucide:book-open-text" },
  // Beer brewing batches
  { title: "Batches", path: "/batches", icon: "lucide:beer" },
  // Inventory
  { title: "Inventory", path: "/inventory", icon: "lucide:clipboard-list" },
  // Suppliers
  { title: "Suppliers", path: "/suppliers", icon: "lucide:store" },
  // Library
  { title: "Library", path: "/library", icon: "lucide:library-big" },
  // Profiles
  { title: "Profiles", path: "/profiles", icon: "ri:contacts-line" },
  // Styles
  { title: "Styles", path: "/styles", icon: "ri:file-list-3-line" },
  // Tools
  { title: "Tools", path: "/tools", icon: "ri:tools-line" },
  // Settings
  { title: "Settings", path: "/settings", icon: "ri:settings-3-line" },
])
</script>

<template>
  <div>
    <header class="flex items-center gap-2 p-4 transition cursor-pointer">
      <Logo />
      <p class="font-bold text-black">HoppyBrew</p>
      <p class="text-sm text-neutral-500">v1.0.0</p>
    </header>
    <div class="px-4 grow">
      <div class="grid gap-2">
        <DropDownCreate />
        <NuxtLink :href="item.path" v-for='(item, index) in items' :key='index'
          class="flex items-center gap-2 px-2 py-1 transition rounded cursor-pointer hover:bg-neutral-100">
          <Icon size="20" :name="item.icon" color="black" />
          <span>{{ item.title }}</span>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>