<template>
  <div id="app">
    <PlayerInfo :players="this.players"/>
    <PlayerInfo :players="this.players"/>
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
      players: null
    }
  },
  created() {
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
  // font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-family:'Courier New', Courier, monospace;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
