<template>
<div>
    <input id="playerInput" type="text" :value="value" v-on="listeners">
    {{ formatDatalist }}
</div>   
</template>

<script>
import Awesomplete from "awesomplete"

export default {
    name: "PlayerInput",
    props: {
        value: {
            type: String,
            default: ""
        },
        datalist: {
            type: Array,
            default: new Array()
        }
    },
    mounted() {
        let input = document.getElementById("playerInput")
        new Awesomplete(input, {minChars: 3, list: this.formatDatalist})
    },
    computed: {
        listeners() {
            return {
                ...this.$listeners,
                input: event => this.$emit("input", event.target.value)
            }
        },
        formatDatalist() {
            var formattedDatalist = []
            for (let entry of this.datalist) {
                formattedDatalist.push(entry["name"])
            }
            return formattedDatalist
        }
    }
}
</script>

<style lang="scss">
    @import "../../node_modules/awesomplete/awesomplete.css";
</style>