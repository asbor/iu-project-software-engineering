<script setup lang="ts">
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
</script>

<template>
    <DropdownMenu>
        <DropdownMenuTrigger>
            <Button class="flex rounded cursor-pointer w-full items-center gap-2 p-2">
                <Icon size="20" name="prime:plus" />
                <span>Create</span>
            </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="w-56">
            <DropdownMenuItem class="flex items-center gap-2">
                <NuxtLink href="/createRecipe"
                    class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                    <Icon size="20" name="prime:plus" />
                    <div class="flex flex-col gap-1">
                        <span>Create</span>
                        <span class="text-xs text-neutral-500">Create a recipe manually</span>
                    </div>
                </NuxtLink>
            </DropdownMenuItem>
            <DropdownMenuItem>
                <NuxtLink href="/ImportXML"
                    class="flex items-center hover:bg-neutral-300 rounded cursor-pointer p-2 gap-2 w-full">
                    <Icon size="20" name="bx:bx-import" />
                    <div class="flex flex-col gap-1">
                        <span>Import</span>
                        <span class="text-xs text-neutral-500">Import BeerXML file</span>
                    </div>
                </NuxtLink>
            </DropdownMenuItem>
        </DropdownMenuContent>
    </DropdownMenu>
</template>