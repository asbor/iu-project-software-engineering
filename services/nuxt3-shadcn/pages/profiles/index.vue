<script>
</script>




<template>
    <div>
        <Equipment>
            <NuxtLink href="/profiles/equipment"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="lucide:cooking-pot" />
                <div class="flex flex-col gap-1">
                    <span>Equipment</span>
                    <span class="text-xs text-neutral-500">Manage equipment repository</span>
                </div>
            </NuxtLink>
        </Equipment>
        <Mash>
            <NuxtLink href="/profiles/mash"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="mi:temperature" />
                <div class="flex flex-col gap-1">
                    <span>Mash</span>
                    <span class="text-xs text-neutral-500">Manage mash profiles</span>
                </div>
            </NuxtLink>
        </Mash>
        <Fermentation>
            <NuxtLink href="/profiles/fermentation"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="material-symbols:fluid-rounded" />
                <div class="flex flex-col gap-1">
                    <span>Fermentation</span>
                    <span class="text-xs text-neutral-500">Manage fermentation profiles</span>
                </div>
            </NuxtLink>
        </Fermentation>
        <Water>
            <NuxtLink href="/profiles/water"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="ph:drop-fill" />
                <div class="flex flex-col gap-1">
                    <span>Water</span>
                    <span class="text-xs text-neutral-500">Manage water profiles</span>
                </div>
            </NuxtLink>
        </Water>
        <CustomStyles>
            <NuxtLink href="/profiles/customStyles"
                class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                <Icon size="40" name="ri:file-list-3-line" />
                <div class="flex flex-col gap-1">
                    <span>Custom Styles</span>
                    <span class="text-xs text-neutral-500">Manage custom beer styles</span>
                </div>
            </NuxtLink>
        </CustomStyles>
    </div>

</template>