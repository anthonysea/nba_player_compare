<template>
    <div id="player-info">
        <PlayerBasicStats
            v-if="this.playerInfo"
            :basic-stats="this.playerInfo"
        />
    </div>
</template>

<script>

const axios = require("axios").default
import PlayerInput from "./PlayerInput"
import PlayerBasicStats from "./PlayerBasicStats"

export default {
    name: "PlayerInfo",
    props: ["playerNameId",],
    components: {
        PlayerBasicStats,
    },
    data() {
        return {
            playerInfo: {}
        }
    },
    watch: {
        playerNameId: {
            immediate: true,
            handler: function(player) {
                var vm = this
                axios.get(`http://localhost:5000/api/commonplayerinfo/${player.id}`)
                .then(function(response) {
                    vm.playerInfo = response.data
                })
            }
        }
    }
}
</script>

<style lang="scss">
    player-info {
        grid-area: p1;
    }
</style>