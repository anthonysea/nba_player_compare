<template>
  <div id="app">
    <PlayerInfo/>
  </div>
</template>

<script>
import PlayerInfo from "./components/PlayerInfo"

export default {
  name: 'app',
  components: {
    PlayerInfo
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
