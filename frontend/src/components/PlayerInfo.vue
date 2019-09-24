<template>
    <div>
        <PlayerInput
            v-model="inputText"
            :datalist="this.playerSearchResults"
            placeholder="Player to search for"
            @keyup="searchForPlayer"
        />
        <p v-if="this.playerSearchResults.length">{{ this.playerSearchResults }}</p>
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
            var fuse = new Fuse(this.players, {keys: ["name"], threshold: 0.5, shouldShort: true})
            this.playerSearchResults = fuse.search(this.inputText).slice(0, 10)
        }, 300)
    },
    data () {
        return {
            inputText: "",
            playerSearchResults: []
        }
    },
}
</script>