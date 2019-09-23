<template>
    <div>
        <PlayerInput
            v-model="inputText"
            placeholder="Player to search for"
            @keydown.enter="searchForPlayer"
        />
        <p>{{ this.data }}</p>
        <div id="player-stats">

        </div>
    </div>
</template>

<script>
const axios = require("axios").default
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
            inputText: "",
            data: {}
        }
    },
    methods: {
        searchForPlayer() {
            var vm = this
            axios.get(`https://www.balldontlie.io/api/v1/players?search=${this.inputText}`)
                .then(function(response) {
                    vm.data = response
                })
        },
    }
}
</script>