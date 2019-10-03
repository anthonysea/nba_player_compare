<template>
  <div id="app">
    <header><h2>NBA Player VS</h2></header>
    <PlayerInfo 
      :players="this.players" 
      datalist-name="playerList1"
      @updateCurrentPlayer="addNewPlayer"
    />
    <PlayerInfo 
      :players="this.players" 
      datalist-name="playerList2"
      @updateCurrentPlayer="addNewPlayer"
    />
    <CareerStats
      v-show="this.comparing"
      :comparing="this.comparing"
    />
  </div>
</template>

<script>
const axios = require("axios").default
import PlayerInfo from "./components/PlayerInfo"
import CareerStats from "./components/CareerStats"

export default {
  name: 'app',
  components: {
    PlayerInfo,
    CareerStats,
  },
  data() {
    return {
      players: null,
      comparing: null,
    }
  },
  created() {
    document.title = "NBA Player VS" 
    var vm = this
    axios.get("http://localhost:5000/api/allplayers")
    .then(function(response) {
      vm.players = response.data
    })
  },
  methods: {
    addNewPlayer(playerId, playerName) {
      this.fetchCareerStats(playerId, playerName)
    },
    fetchCareerStats(playerId, playerName) {
      var vm = this
      axios.get(`http://localhost:5000/api/careerstats/${playerId}`)
      .then(function(response) {
        if (!vm.comparing) {
          vm.comparing = {}
        }
        vm.$set(vm.comparing, playerId, response.data)
        vm.comparing[playerId].unshift(playerName)
      })
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
  grid-template-columns: 50% 50%;
  grid-template-rows: auto;
  grid-template-areas:
    "header header"
    "p1 p1"
    "career-stats career-stats";
}

header {
  grid-area: header;
}

#career-stats {
  grid-area: career-stats;
}

td {
  padding: 4px;
}
</style>
