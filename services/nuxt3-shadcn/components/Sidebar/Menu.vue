<template>
  <div>
    <header class="flex items-center gap-2 p-4 transition cursor-pointer">
      <Logo />
      <h2 class="font-bold">HoppyBrew</h2>
      <p class="text-sm text-neutral-500">v1.0.0</p>
    </header>
    <main class="px-4 grow">
      <div class="grid gap-2">
        <DropDownCreate />
        <NuxtLink :href="item.path" v-for='(item, index) in items' :key='index'
          class="flex items-center gap-2 px-2 py-1 transition rounded cursor-pointer hover:bg-neutral-100 hover:text-neutral-900">
          <Icon size="20" :name="item.icon" />
          <span>{{ item.title }}</span>
          <!-- Add @click event to call handleLinkClick function -->
        </NuxtLink>
      </div>
    </main>
    <footer>
      <div>
        <div class="p-4">
          <button @click="toggleDark()" class="flex items-center gap-2">
            <Icon :name="isDark.value ? 'bx:bx-moon' : 'bx:bx-sun'" />
            <span>Toggle Color Mode</span>
          </button>
          <CheckDatabaseConnection />
        </div>
        <UserAccountUserItem />
      </div>
    </footer>
  </div>
</template>

<script setup>
props: {
  closeOverlay: Function
};

import { defineEmits } from 'vue';

defineEmits(['linkClicked']);

import Button from '../ui/button/Button.vue';

const items = ref([
  // Dashboard
  { title: "Dashboard", path: "/", icon: "ri:dashboard-line" },
  // Beer brewing recipe
  { title: "Recipe", path: "/recipe", icon: "lucide:book-open-text" },
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

import { useDark, useToggle } from "@vueuse/core";

const isDark = useDark();

</script>
