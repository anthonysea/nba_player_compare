<template>
<div>
    <input name="playerInput" autocomplete="off" id="playerInput" type="text" :value="value" v-on="listeners" :list="this.datalistName"/>
    <datalist :id="this.datalistName">
        <option v-for="player in datalist" :key="player.id" :value="player.name"> {{ player.name }}</option>
    </datalist>
</div>   
</template>

<script>
export default {
    name: "PlayerInput",
    props: {
        value: {
            type: String,
            default: "",
        },
        datalist: {
            type: Array,
            default: new Array()
        },
        datalistName: {
            type: String,
        }
    },
    data() {
        return {
            playerOption: ""
        }
    },
    computed: {
        listeners() {
            return {
                ...this.$listeners,
                input: event => this.$emit("input", event.target.value)
            }
        },
    }
}
</script>