<template>
    <div class="border-2 p-4">
        <header>
            <h2 class="text-xl font-semibold">Inventory</h2>
        </header>
        <div>
            <table class="min-w-full divide-y divide-gray-200">
                <thead>
                    <tr>
                        <th></th>
                        <th>Name</th>
                        <th>Quantity</th>
                        <th>Stock Level</th>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="fermentable in batch.inventory_fermentables" :key="fermentable.id">
                        <tr>
                            <Icon size="20" name="mdi:wheat" />
                            <td>{{ fermentable.name }}</td>
                            <td>{{ fermentable.amount }}</td>
                            <td>{{ fermentable.inventory }}</td>
                        </tr>
                    </template>
                    <template v-for="hop in batch.inventory_hops" :key="hop.id">
                        <tr>
                            <Icon size="20" name="mdi:hops" />
                            <td>{{ hop.name }}</td>
                            <td>{{ hop.amount }}</td>
                            <td>{{ hop.inventory }}</td>
                        </tr>
                    </template>
                    <template v-for="misc in batch.inventory_miscs" :key="misc.id">
                        <tr>
                            <Icon size="20" name="healthicons:sugar-alt" />
                            <td>{{ misc.name }}</td>
                            <td>{{ misc.amount }}</td>
                            <td>{{ misc.inventory }}</td>
                        </tr>
                    </template>
                    <template v-for="yeast in batch.inventory_yeasts" :key="yeast.id">
                        <tr>
                            <Icon size="20" name="mdi:yeast" />
                            <td>{{ yeast.name }}</td>
                            <td>{{ yeast.amount }}</td>
                            <td>{{ yeast.inventory }}</td>
                        </tr>
                    </template>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        batch: {
            type: Object,
            required: true
        }
    }
};
</script>

<style scoped>
table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #f2f2f2;
}
</style>