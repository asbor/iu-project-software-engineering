<script setup>
const loading = ref(false)
</script>

<template>
    <div class="grid w-full gap-4">
        <header class="flex items-start justify-between">
            <div class="grow">
                <h1>Create Recipes</h1>
            </div>
        </header>

        <main class="grid w-full gap-4">
            <div class="flex items-start justify-between border-2 border-black gap-2">
                <div name="Image Section" class="border-2 border-black items-center w-full gap-1">
                    <div>
                        <Icon size="150" name="ri:beer-fill" />
                    </div>
                    <Button class="items-center gap-2">
                        <Icon size="20" name="ph:image" />
                        <p>Add Image</p>
                    </Button>
                </div>
                <div name="Metadata" class="border-2 border-black w-full gap-2">
                    <div>
                        <div>
                            <label for="RecipeName" class="form-label">Name:</label>
                        </div>
                        <div>
                            <input type="text" name="RecipeName" class="form-control" placeholder="Recipe Name">

                        </div>
                    </div>
                    <hr style="border-bottom: 1px solid lightgray;" />
                    <div>
                        <div>
                            <label for="RecipeAuthor" class="form-label">Author:</label>
                        </div>
                        <div>
                            <input type="text" name="RecipeAuthor" class="form-control" placeholder="Author's Name">
                        </div>
                    </div>
                    <hr style="border-bottom: 1px solid lightgray;" />
                    <div>
                        Type
                    </div>
                </div>
                <div name="Equipment Style" class="border-2 border-black w-full gap-2">
                    <div class="w-full gap-2">
                        <div class="flex items-start items-center gap-2">
                            <div>
                                <Icon size="40" name="game-icons:cooking-pot" />
                            </div>
                            <div>
                                <label for="Equipment" class="form-label">Equipment:</label>
                            </div>
                        </div>
                        <hr style="border-bottom: 1px solid lightgray;" />
                        <div>
                            <h2 class="text-lg font-bold text-neutral-400">Brewster Becacon 70L</h2>
                        </div>
                        <div class="flex items-start items-center gap-2">
                            <div>
                                <Icon size="20" name="heroicons-solid:beaker" />
                            </div>
                            <div>
                                <label for="BatchVolume" class="form-label">Batch Volume:</label>
                            </div>
                            <div>
                                <p>20L</p>
                            </div>
                        </div>
                        <div class="flex items-start items-center gap-2">
                            <div>
                                <Icon size="20" name="gravity-ui:stopwatch" />
                            </div>
                            <div>
                                <label for="BoilTime" class="form-label">Boil Time:</label>
                            </div>
                            <div>
                                <p>60 min</p>
                            </div>
                        </div>
                        <div class="flex items-start items-center gap-2">
                            <div>
                                <Icon size="20" name="heroicons-solid:fire" />
                            </div>
                            <div>
                                <label for="Pre-Boil Volume" class="form-label">Pre-Boil Volume:</label>
                            </div>
                            <div>
                                <p>25L</p>
                            </div>
                        </div>
                        <div class="flex items-start items-center gap-2">
                            <div>
                                <Icon size="20" name="heroicons-solid:fire" />
                            </div>
                            <div>
                                <label for="Brewhouse Efficiency" class="form-label">Brewhouse Efficiency:</label>
                            </div>
                            <div>
                                <p>75%</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="w-full gap-2">
                    <div class="flex items-start items-center gap-2">
                        <div>
                            <Icon size="20" name="ion:book-sharp" />
                        </div>
                        <div>
                            <label for="Style" class="form-label">Style:</label>
                        </div>
                        <div class="bg-neutral-300 rounded w-40 p-2 items-center gap-2">
                            <button class="btn btn-primary">SELECT</button>
                        </div>
                    </div>
                    <div>
                        <div class="flex items-start items-center gap-2">
                            <div class="w-[50px]">
                                <label for="Description" class="form-label">ABV:</label>
                            </div>
                            <div class="w-full gap-2 bg-green-300 rounded p-2">
                                <h2>5.5%</h2>
                            </div>
                        </div>
                        <div class="flex items-start items-center gap-2">
                            <div class="w-[50px]">
                                <label for="Description" class="form-label">OG:</label>
                            </div>
                            <div class="w-full gap-2 bg-green-300 rounded p-2">
                                <h2>5.5%</h2>
                            </div>
                        </div>
                        <div class="flex items-start items-center gap-2">
                            <div class="w-[50px]">
                                <label for="Description" class="form-label">FG:</label>
                            </div>
                            <div class="w-full gap-2 bg-green-300 rounded p-2">
                                <h2>5.5%</h2>
                            </div>
                        </div>
                        <div class="flex items-start items-center gap-2">
                            <div class="w-[50px]">
                                <label for="Description" class="form-label">ECB:</label>
                            </div>
                            <div class="w-full gap-2 bg-green-300 rounded p-2">
                                <h2>5.5%</h2>
                            </div>
                        </div>
                        <div class="flex items-start items-center gap-2">
                            <div class="w-[50px]">
                                <label for="Description" class="form-label">IBU:</label>
                            </div>
                            <div class="w-full gap-2 bg-green-300 rounded p-2">
                                <h2>5.5%</h2>
                            </div>
                        </div>
                        <div class="flex items-start items-center gap-2">
                            <div class="w-[50px]">
                                <label for="Description" class="form-label">BU/GU:</label>
                            </div>
                            <div class="w-full gap-2 bg-green-300 rounded p-2">
                                <h2>5.5%</h2>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex items-start justify-between border-2 border-black gap-2">
                <div>
                    <div class="flex items-start items-center gap-2 w-full">
                        <div>
                            <Icon size="20" name="lucide:wheat" />
                        </div>
                        <div>
                            <label for="Fermentables" class="form-label">Fermentables:</label>
                        </div>
                    </div>
                    <div class="flex items-start items-center gap-2 w-full">
                        <div>
                            <Icon size="20" name="lucide:hop" />
                        </div>
                        <div>
                            <label for="Hops" class="form-label">Hops:</label>
                        </div>
                    </div>
                    <div class="flex items-start items-center gap-2 w-full">
                        <div>
                            <Icon size="20" name="game-icons:cool-spices" />
                        </div>
                        <div>
                            <label for="Misc" class="form-label">Misc:</label>
                        </div>
                    </div>
                    <div class="flex items-start items-center gap-2 w-full">
                        <div>
                            <Icon size="20" name="heroicons-solid:beaker" />
                        </div>
                        <div>
                            <label for="Yeast" class="form-label">Yeast:</label>
                        </div>
                    </div>
                    <div class="flex items-start items-center gap-2 w-full">
                        <div>
                            <Icon size="20" name="mdi:water-temperature-outline" />
                        </div>
                        <div>
                            <label for="MashProfile" class="form-label">Mash Profile:</label>
                        </div>
                    </div>
                    <div class="flex items-start items-center gap-2 w-full">
                        <div>
                            <Icon size="20" name="lucide:wheat" />
                        </div>
                        <div>
                            <label for="FermentationProfile" class="form-label">Fermentation Profile:</label>
                        </div>
                    </div>
                    <div class="flex items-start items-center gap-2 w-full">
                        <div>
                            <Icon size="20" name="ion:water-outline" />
                        </div>
                        <div>
                            <label for="WaterProfile" class="form-label">Water Profile:</label>
                        </div>
                    </div>
                    <div class="flex items-start items-center gap-2 w-full">
                        <div>
                            <Icon size="20" name="material-symbols-light:other-admission-outline-sharp" />
                        </div>
                        <div>
                            <label for="Other" class="form-label">Other</label>
                        </div>
                    </div>
                </div>
            </div>
            <div class="border-2 border-black gap-2">
                <div>
                    <label for="Tags" class="form-label">Tags:</label>
                </div>
                <div>
                    <Input class="w-full" placeholder="Add Tags" />
                </div>
            </div>
            <div class="border-2 border-black gap-2">
                <div>
                    <label for="Notes" class="form-label">Notes:</label>
                </div>
                <div>
                    <Input class="w-full" placeholder="Special notes about this recipe..." />
                </div>
            </div>
        </main>
        <footer>
        </footer>
    </div>

</template>