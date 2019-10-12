<template>
  <div id="app">
    <header><h2>NBA Player VS</h2></header>
    <PlayerInput
      id="player-input"
      v-model="inputText"
      :datalist="this.playerSearchResults"
      placeholder="Player to search for"
      @input="this.searchForPlayer"
      @keyup.enter="addNewPlayer"
    />
    <PlayerInfo 
      v-for="player in playerNamesIds"
      :player-name-id="player"
      :key="player.id"
      @remove-player="removePlayerFn"
    />
    <CareerStats
      v-show="this.comparing"
      :comparing="this.comparing"
    />
    <select v-show="this.comparing" v-model="statType" id="stat-list" name="stat-list">
      <option v-for="stat in statTypes" :value="stat" :key="stat.name">{{ stat.toUpperCase() }}</option>
    </select>

    <select v-show="this.comparing" v-model="regularSeasonBool" name="regular-season-bool" id="regular-season-bool">
      <option :value="true">Regular Season</option>
      <option :value="false">Post Season</option>
    </select>

    <StatsGraph
      id="stats-graph"
      v-show="this.comparing"
      :comparing="this.comparing"
      :stat="statType"
      :regular-season-bool="this.regularSeasonBool"
    />


  </div>
</template>

<script>
const axios = require("axios").default
var _ = require('lodash')
const Fuse = require('fuse.js')
import PlayerInfo from "./components/PlayerInfo"
import CareerStats from "./components/CareerStats"
import PlayerInput from "./components/PlayerInput"
import StatsGraph from "./components/StatsGraph"
import Vue from 'vue'

export default {
  name: 'app',
  components: {
    PlayerInput,
    PlayerInfo,
    CareerStats,
    StatsGraph,
  },
  data() {
    return {
      playersToSearch: null,
      comparing: null,
      inputText: "",
      playerNamesIds: [],
      playerSearchResults: [],
      statTypes: ["gp", "gs", "min", "fgm", "fga", "fg_pct", "fg3m", "fg3a", "fg3_pct", "ftm", "fta", "ft_pct", "oreb", "dreb", "reb", 
                  "ast", "stl", "blk", "tov", "pf", "pts"],
      statType: "pts",
      regularSeasonBool: true,
    }
  },
  created() {
    document.title = "NBA Player VS" 
    var vm = this
    axios.get("http://localhost:5000/api/allplayers")
    .then(function(response) {
      vm.playersToSearch = response.data
    })
  },
  methods: {
    searchForPlayer: _.debounce(function() {
            var fuse = new Fuse(this.playersToSearch, {keys: ["name"], threshold: 0.5, shouldShort: true})
            this.playerSearchResults = fuse.search(this.inputText).slice(0, 10)
        }, 300),
    addNewPlayer(playerId, playerName) {
      // Check to see if player has already been added & that there are less than 6 players already being compared
      if (!this.playerNamesIds.includes(this.playerSearchResults[0]) && (this.playerNamesIds.length < 6)) {
        this.playerNamesIds.push(this.playerSearchResults[0])
        this.fetchCareerStats(this.playerSearchResults[0])
      }
      
    },
    fetchCareerStats(player) {
      var vm = this
      // console.log(JSON.stringify(player))
      axios.get(`http://localhost:5000/api/careerstats/${player.id}`)
      .then(function(response) {
        if (!vm.comparing) {
          vm.comparing = {}
        }
        vm.$set(vm.comparing, player.id, response.data)
        vm.comparing[player.id].unshift(player.name)
      })
    },
    removePlayerFn(playerId) {
      this.playerNamesIds = this.playerNamesIds.filter(player => player.id !== playerId)
      // Reactive method for deleting properties of objects
      Vue.delete(this.comparing, playerId)
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family:'Courier New', Courier, monospace;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0 auto;
  max-width: 80em;

  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: auto;
  grid-template-areas:
    "header header header"
    "input input input"
    "p1 p1 p1"
    "p1 p1 p1"
    "career-stats career-stats career-stats"
    "stat-list stat-list regular-season-bool"
    "stats-graph stats-graph stats-graph"
}

header {
  grid-area: header;
}

#career-stats {
  grid-area: career-stats;
}

#player-input {
  grid-area: input;
}

td {
  padding: 4px;
}

#stat-list {
  grid-area: stat-list;
}

#regular-season-bool {
  grid-area: regular-season-bool;
}

#stats-graph {
  grid-area: stats-graph;
}
</style>
