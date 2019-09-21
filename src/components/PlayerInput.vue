<template>
    <input type="text" :value="value" v-on="listeners">
</template>

<script>
export default {
    name: "PlayerInput",
    props: {
        value: {
            type: String,
            default: ""
        }
    },
    computed: {
        listeners() {
            return {
                ...this.$listeners,
                input: event => this.$emit("input", event.target.value)
            }
        }
    }
}
</script>