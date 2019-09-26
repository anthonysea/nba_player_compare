<template>
    <div>
        <PlayerInput
            v-model="inputText"
            :datalist="this.playerSearchResults"
            placeholder="Player to search for"
            @input="searchForPlayer"
            @keyup.enter="updateCurrentPlayer"
        />
        <!-- <p v-if="this.playerSearchResults.length">{{ this.playerSearchResults }}</p> -->
        {{ this.currentPlayer }}
        {{ this.commonPlayerInfo }}
        {{ this.careerStats }}
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
        }, 300),
        updateCurrentPlayer() {
            this.currentPlayer = this.playerSearchResults[0]
            this.fetchCommonPlayerInfo()
            this.fetchCareerStats()
        },
        fetchCommonPlayerInfo() {
            var vm = this
            axios.get(`http://localhost:5000/api/commonplayerinfo/${this.currentPlayer.id}`)
            .then(function(response) {
                vm.commonPlayerInfo = response.data
            })
        },
        fetchCareerStats() {
            var vm = this
            axios.get(`http://localhost:5000/api/careerstats/${this.currentPlayer.id}`)
            .then(function(response) {
                vm.careerStats = response.data
            })
        }
    },
    data () {
        return {
            inputText: "",
            playerSearchResults: [],
            currentPlayer: {},
            commonPlayerInfo: null,
            careerStats: null,
        }
    },
}
</script>