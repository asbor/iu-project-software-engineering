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
        <NuxtLink :href="item.path" v-for="(item, index) in items" :key="index"
          class="flex items-center gap-2 px-2 py-1 transition rounded cursor-pointer hover:bg-neutral-100 hover:text-neutral-900">
          <Icon size="20" :name="item.icon" />
          <span>{{ item.title }}</span>
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
import { ref } from 'vue';
import { useDark, useToggle } from '@vueuse/core';
import Logo from '@/components/Logo.vue';
import DropDownCreate from '@/components/DropDown/Create.vue';
import CheckDatabaseConnection from '@/components/checkDatabaseConnection.vue';
import UserAccountUserItem from '@/components/UserAccount/UserItem.vue';

const items = ref([
  { title: 'Dashboard', path: '/', icon: 'ri:dashboard-line' },
  { title: 'Recipes', path: '/recipes', icon: 'lucide:book-open-text' },
  { title: 'Batches', path: '/batches', icon: 'lucide:beer' },
  { title: 'Inventory', path: '/inventory', icon: 'lucide:clipboard-list' },
  { title: 'References', path: '/references', icon: 'lucide:store' },
  { title: 'Library', path: '/library', icon: 'lucide:library-big' },
  { title: 'Profiles', path: '/profiles', icon: 'ri:contacts-line' },
  { title: 'Styles', path: '/styles', icon: 'ri:file-list-3-line' },
  { title: 'Tools', path: '/tools', icon: 'ri:tools-line' },
  { title: 'Settings', path: '/settings', icon: 'ri:settings-3-line' },
  { title: 'Log', path: '/log', icon: 'ri:file-list-3-line' },
  { title: 'About', path: '/about', icon: 'ri:information-line' },
]);

const emit = defineEmits(['linkClicked']);

const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>
