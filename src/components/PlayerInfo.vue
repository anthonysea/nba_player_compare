<template>
    <div>
        <PlayerInput
            v-model="inputText"
            placeholder="Player to search for"
            @keydown.enter="searchForPlayer"
        />
        <p>{{ this.inputText }}</p>
    </div>
</template>

<script>
import PlayerInput from "./PlayerInput"
import PlayerBasicStats from "./PlayerBasicStats"
import PlayerCareerSummary from "./PlayerCareerSummary"

export default {
    name: "PlayerInfo",
    components: {
        PlayerInput,
        PlayerBasicStats,
        PlayerCareerSummary,
    },
    data () {
        return {
            inputText: ""
        }
    },
    methods: {
        searchForPlayer() {
            this.inputText = "enter pressed"
        },
    }
}
</script>