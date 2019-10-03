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

export default {
    name: "PlayerInfo",
    props: ["players", "datalistName"],
    components: {
        PlayerInput,
        PlayerBasicStats,
    },
    methods: {
        searchForPlayer: _.debounce(function() {
            var fuse = new Fuse(this.players, {keys: ["name"], threshold: 0.5, shouldShort: true})
            this.playerSearchResults = fuse.search(this.inputText).slice(0, 10)
        }, 300),
        updateCurrentPlayer() {
            this.currentPlayer = this.playerSearchResults[0]
            this.fetchCommonPlayerInfo()
            this.$emit('updateCurrentPlayer', this.currentPlayer.id, this.currentPlayer.name)
            // this.$root.$emit('updateCurrentPlayer', this.currentPlayer.name)
        },
        fetchCommonPlayerInfo() {
            var vm = this
            axios.get(`http://localhost:5000/api/commonplayerinfo/${this.currentPlayer.id}`)
            .then(function(response) {
                vm.commonPlayerInfo = response.data
            })
        },
    },
    data () {
        return {
            inputText: "",
            playerSearchResults: [],
            currentPlayer: {},
            commonPlayerInfo: null,
        }
    },
}
</script>

<style lang="scss">
    player-info {
        grid-area: p1;
    }
</style>