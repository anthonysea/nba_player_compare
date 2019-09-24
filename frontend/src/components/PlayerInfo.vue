<template>
    <div>
        <PlayerInput
            v-model="inputText"
            placeholder="Player to search for"
            @keyup="searchForPlayer"
        />
        <p v-if="this.currentPlayer">{{ this.currentPlayer }}</p>
        <div id="player-stats">
            
        </div>
    </div>
</template>

<script>
var _ = require('lodash')
const Fuse = require('fuse.js')
const axios = require("axios").default
import PlayerInput from "./PlayerInput"
import PlayerBasicStats from "./PlayerBasicStats"
import PlayerCareerSummary from "./PlayerCareerSummary"

export default {
    name: "PlayerInfo",
    props: ['players'],
    components: {
        PlayerInput,
        PlayerBasicStats,
        PlayerCareerSummary,
    },
    methods: {
        searchForPlayer: _.debounce(function() {
            var fuse = new Fuse(this.players, {keys: ["name"]})
            this.currentPlayer = fuse.search(this.inputText)
        }, 300)
    },
    data () {
        return {
            inputText: "",
            currentPlayer: null
        }
    },
}
</script>