<script>
export default {
    props: {
        title: {
            type: String,
            default: 'Loading'
        }
    }
}
</script>

<template>
    <div>
        <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden">Loading...</span>
        </div> {{ title }}...
    </div>
</template>