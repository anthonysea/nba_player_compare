<template>
    <div @mouseover="hover=true" @mouseleave="hover=false">
        <h4 id="player-name">{{ this.name }} <span @click="$emit('remove-player', playerNameId.id)" v-if="hover" id="remove-button">[x]</span></h4>
        <span id="birth-date">Birthdate: </span>{{ this.birthdate }}<br/>
        <span id="country">Country: </span>{{ this.country }}<br/>
        <span id="height">Height: </span> {{ this.height }}<br/>
        <span id="weight">Weight: </span>{{ this.weight }} lbs<br/>
        <span id="jersey-number">Number: </span>{{ this.number }} <br/>
        <span id="years-in-league">Years In League: </span>{{ this.yearsInLeague }} <br/>
        <span id="position">Position: </span>{{ this.position }} <br/>
        <span id="rosterStatus">Roster Status: </span>{{ this.rosterStatus }} <br/>
        <span id="team">Team: </span>{{ this.team }} <br/>
        <span id="fromYear">Played From: </span> {{ this.fromYear }} <br/>
        <span id="toYear">Played To: </span>{{ this.toYear }} <br/>   
        <span id="draft-year">Draft Year: </span>{{ this.draftYear }} <br/>
        <span id="draft-round">Draft Round: </span>{{ this.draftRound }} <br/>
        <span id="draft-number">Draft Number: </span> {{ this.draftNumber }} <br/>
    </div>
</template>

<script>

const axios = require("axios").default

export default {
    name: "PlayerInfo",
    props: ["playerNameId",],

    data() {
        return {
            // playerInfo: {},
            hover: false,
            name: "",
            birthdate: "",
            college: "",
            lastAffiliation: "",
            country: "",
            height: "",
            weight: "",
            number: "",
            yearsInLeague: "",
            position: "",
            rosterStatus: "",
            team: "",
            fromYear: "",
            toYear: "",
            draftYear: "",
            draftRound: "",
            draftNumber: "",
        }
    },
    watch: {
        playerNameId: {
            immediate: true,
            handler: function(player) {
                var vm = this
                axios.get(`http://localhost:5000/api/commonplayerinfo/${player.id}`)
                .then(function(response) {
                    // vm.playerInfo = response.data
                    vm.name = response.data['rowSet'][0][3]
                    vm.birthdate = response.data['rowSet'][0][6]
                    vm.country = response.data['rowSet'][0][8]
                    vm.college = response.data['rowSet'][0][7]
                    vm.lastAffiliation = response.data['rowSet'][0][9]
                    vm.height = response.data['rowSet'][0][10]
                    vm.weight = response.data['rowSet'][0][11]
                    vm.number = response.data['rowSet'][0][13]
                    vm.position = response.data['rowSet'][0][14]
                    vm.yearsInLeague = response.data['rowSet'][0][12]
                    vm.rosterStatus = response.data['rowSet'][0][15]
                    vm.team = `${response.data['rowSet'][0][20]} ${response.data['rowSet'][0][17]}`
                    vm.fromYear = response.data['rowSet'][0][22]
                    vm.toYear = response.data['rowSet'][0][23]
                    vm.draftYear = response.data['rowSet'][0][27]
                    vm.draftRound = response.data['rowSet'][0][28]
                    vm.draftNumber = response.data['rowSet'][0][29]
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