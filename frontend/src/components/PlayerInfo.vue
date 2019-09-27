<template>
    <div id="player-info">
        <PlayerInput
            v-model="inputText"
            :datalist="this.playerSearchResults"
            :datalist-name="this.datalistName"
            placeholder="Player to search for"
            @input="this.searchForPlayer"
            @keyup.enter="updateCurrentPlayer"
        />
        <PlayerBasicStats
            v-if="this.commonPlayerInfo"
            :basic-stats="this.commonPlayerInfo"
        />
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
    props: ["players", "datalistName"],
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
        async updateCurrentPlayer() {
            this.currentPlayer = this.playerSearchResults[0]
            await this.fetchCommonPlayerInfo()
            await this.fetchCareerStats()
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

<style lang="scss">
    player-info {
        grid-area: p1;
    }
</style>