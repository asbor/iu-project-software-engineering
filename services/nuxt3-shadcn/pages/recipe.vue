<script setup>
const loading = ref(false)
let data = ref([])


const cards = [
    {
        icon: "bx:bx-beer",
        color: "bg-green-400",
        title: "Tripel Westmalle",
        author: "Asbjorn Bordoy",
        label: "Belgian Tripel (All Grain)",
        ABV: 8.0 + "%",
        OG: 1.080 + "/" + 19.3 + "°P",
        FG: 1.012 + "/" + 3.1 + "°P",
        IBU: 36,
        tags: ["#Belgian", "#Tripel", "#All Grain"],
        likes: 12,
        views: 124,
        downloads: 4
    },
    {
        icon: "bx:bx-beer",
        color: "bg-green-400",
        title: "IPA",
        author: "Asbjorn Bordoy",
        label: "American IPA (Extract)",
        ABV: 6.5 + "%",
        OG: 1.065 + "/" + 16.0 + "°P",
        FG: 1.012 + "/" + 3.1 + "°P",
        IBU: 60,
        tags: ["#American", "#IPA", "#Extract"],
        likes: 12,
        views: 124,
        downloads: 4
    },
    {
        icon: "bx:bx-beer",
        color: "bg-green-400",
        title: "Stout",
        author: "Asbjorn Bordoy",
        label: "Irish Stout (All Grain)",
        ABV: 4.5 + "%",
        OG: 1.045 + "/" + 11.3 + "°P",
        FG: 1.010 + "/" + 2.6 + "°P",
        IBU: 35,
        tags: ["#Irish", "#Stout", "#All Grain"],
        likes: 12,
        views: 124,
        downloads: 4
    },
    {
        icon: "bx:bx-beer",
        color: "bg-green-400",
        title: "Pilsner",
        author: "Asbjorn Bordoy",
        label: "German Pilsner (Extract)",
        ABV: 5.0 + "%",
        OG: 1.050 + "/" + 12.5 + "°P",
        FG: 1.010 + "/" + 2.6 + "°P",
        IBU: 40,
        tags: ["#German", "#Pilsner", "#Extract"],
        likes: 12,
        views: 124,
        downloads: 4
    },
    {
        icon: "bx:bx-beer",
        color: "bg-green-400",
        title: "Pale Ale",
        author: "Asbjorn Bordoy",
        label: "American Pale Ale (All Grain)",
        ABV: 5.5 + "%",
        OG: 1.055 + "/" + 13.7 + "°P",
        FG: 1.012 + "/" + 3.1 + "°P",
        IBU: 40,
        tags: ["#American", "#Pale Ale", "#All Grain"],
        likes: 12,
        views: 124,
        downloads: 4
    }

]


</script>

<template>
    <div class="grid w-full gap-4">
        <header class="flex items-start justify-between">
            <div class="grow">
                <h1>Recipe</h1>
            </div>
            <ProductNewDialog />
            <UserAccountLoginDialog />
        </header>
        <main class="grid w-full gap-4">
            <div>
                <input type="text" placeholder="Search for recipe"
                    class="w-full p-2 border border-neutral-200 rounded bg-neutral-200" />
            </div>
            <div class="grid gap-4 lg:grid-cols-4">
                <BeerCard v-for='( item, index ) in cards' :card="item" :key='index' />
            </div>
        </main>
        <footer>
            <Pagination />

            <div class="flex items-center justify-end gap-2">
                <Button variant="outline">Previous</Button>
                <Button variant="outline">Next</Button>
            </div>
            <div class="flex items-center justify-end gap-2">
                <Button variant="outline">1</Button>
                <Button variant="outline">2</Button>
                <Button variant="outline">3</Button>
                <Button variant="outline">4</Button>
                <Button variant="outline">5</Button>
            </div>
        </footer>
    </div>
</template>