<template>
  <div id="app">
    <header><h2>NBA Player VS</h2></header>
    <PlayerInfo :players="this.players" datalist-name="playerList1"/>
    <PlayerInfo :players="this.players" datalist-name="playerList2"/>
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
      players: null,
      comparing: []
    }
  },
  created() {
    document.title = "NBA Player VS"
    var vm = this
    axios.get("http://localhost:5000/api/allplayers")
    .then(function(response) {
      vm.players = response.data
    })
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
  max-width: 110em;

  display: grid;
  grid-template-columns: 50% 50%;
  grid-template-rows: auto;
  grid-template-areas:
    "header header"
    "p1 p1"
    "p1 p1";
}

header {
  grid-area: header;
}
</style>
