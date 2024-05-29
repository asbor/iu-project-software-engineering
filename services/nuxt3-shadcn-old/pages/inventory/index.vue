<script>
</script>




<template>
    <div>
        <Fermentable>
            <NuxtLink href="/inventory/fermentables"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="mdi:wheat" />
                <div class="flex flex-col gap-1">
                    <span>Fermentables</span>
                    <span class="text-xs text-neutral-500">Manage fermentable</span>
                </div>
            </NuxtLink>
        </Fermentable>
        <Hop>
            <NuxtLink href="/inventory/hops"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="mdi:hops" />
                <div class="flex flex-col gap-1">
                    <span>Hops</span>
                    <span class="text-xs text-neutral-500">Manage hops</span>
                </div>
            </NuxtLink>
        </Hop>
        <Misc>
            <NuxtLink href="/inventory/miscs"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="healthicons:sugar-alt" />
                <div class="flex flex-col gap-1">
                    <span>Miscs</span>
                    <span class="text-xs text-neutral-500">Manage misc</span>
                </div>
            </NuxtLink>
        </Misc>
        <Yeast>
            <NuxtLink href="/inventory/yeasts"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="mdi:yeast" />
                <div class="flex flex-col gap-1">
                    <span>Yeasts</span>
                    <span class="text-xs text-neutral-500">Manage yeast</span>
                </div>
            </NuxtLink>
        </Yeast>
    </div>

</template>