<script setup>
import { ref } from 'vue';
import { useDark } from '@vueuse/core';

const open = ref(true);
const isDark = useDark();

const toggleOverlay = () => {
  open.value = !open.value;
};

const closeOverlay = () => {
  console.log('Overlay closed');
  open.value = false;
};
</script>

<template>
  <div>
    <div class="z-50 flex items-center justify-between w-full h-full p-4 lg:hidden">
      <Logo />
      <div>
        <Icon class="z-50 cursor-pointer left-2 top-2" size="30" name="iconamoon:menu-burger-horizontal"
          @click="open = true" />
      </div>

      <div name="overlay" v-if="open" :class="{ 'bg-white': !isDark, 'bg-gray-800': isDark }"
        class="fixed top-0 left-0 z-[999] w-full h-full h-screen">
        <Icon class="absolute z-50 cursor-pointer right-4 top-4" size="30" name="material-symbols:close"
          @click="open = false" />
        <SidebarMenu @linkClicked="closeOverlay" />
      </div>
    </div>
    <div class="hidden lg:flex w-[250px] h-screen flex flex-col justify-between border-r">
      <SidebarMenu />
    </div>
  </div>
</template>
