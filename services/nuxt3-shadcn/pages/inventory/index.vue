<script>
</script>




<template>
    <div>
        <Fermentable>
            <NuxtLink href="/inventory/fermentable"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="mdi:wheat" />
                <div class="flex flex-col gap-1">
                    <span>Fermentable</span>
                    <span class="text-xs text-neutral-500">Manage fermentable</span>
                </div>
            </NuxtLink>
        </Fermentable>
        <Hop>
            <NuxtLink href="/inventory/hop"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="mdi:hops" />
                <div class="flex flex-col gap-1">
                    <span>Hop</span>
                    <span class="text-xs text-neutral-500">Manage hop</span>
                </div>
            </NuxtLink>
        </Hop>
        <Misc>
            <NuxtLink href="/inventory/misc"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="healthicons:sugar-alt" />
                <div class="flex flex-col gap-1">
                    <span>Misc</span>
                    <span class="text-xs text-neutral-500">Manage misc</span>
                </div>
            </NuxtLink>
        </Misc>
        <Yeast>
            <NuxtLink href="/inventory/yeast"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="mdi:yeast" />
                <div class="flex flex-col gap-1">
                    <span>Yeast</span>
                    <span class="text-xs text-neutral-500">Manage yeast</span>
                </div>
            </NuxtLink>
        </Yeast>
    </div>

</template>