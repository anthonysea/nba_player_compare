<template>
  <div id="app">
    <PlayerInfo/>
    {{ this.players }}
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
  mounted() {
    var vm = this
    axios.get("http://localhost:5000/api/allplayers")
    .then(function(response) {
      vm.players = response
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
