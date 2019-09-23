<template>
  <div id="app">
    <PlayerInfo/>
  </div>
</template>

<script>
const axios = require("axios").default
import PlayerInfo from "./components/PlayerInfo"

export default {
  name: 'app',
  components: {
    PlayerInfo
  },
  data() {
    return {
      allPlayerInfo: {}
    }
  },
  mounted() {
    // Get info for all players
    axios.get("https://stats.nba.com/stats/commonallplayers?LeagueID=00&Season=2018-19&IsOnlyCurrentSeason=0", {
      crossdomain: true
    })
      .then(function(response) {
        // handle success
        this.allPlayerInfo = response
      })
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
