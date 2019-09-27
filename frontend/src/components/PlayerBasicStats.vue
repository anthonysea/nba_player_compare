<template>
    <div>
        <h4 id="player-name">{{ this.name }}</h4>
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
export default {
    props: ['basicStats'],
    data() {
        return {
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
        basicStats: function(newVal, oldVal) {
            this.name = newVal['rowSet'][0][3]
            this.birthdate = newVal['rowSet'][0][6]
            this.country = newVal['rowSet'][0][8]
            this.college = newVal['rowSet'][0][7]
            this.lastAffiliation = newVal['rowSet'][0][9]
            this.height = newVal['rowSet'][0][10]
            this.weight = newVal['rowSet'][0][11]
            this.number = newVal['rowSet'][0][13]
            this.position = newVal['rowSet'][0][14]
            this.yearsInLeague = newVal['rowSet'][0][12]
            this.rosterStatus = newVal['rowSet'][0][15]
            this.team = `${newVal['rowSet'][0][20]} ${newVal['rowSet'][0][17]}`
            this.fromYear = newVal['rowSet'][0][22]
            this.toYear = newVal['rowSet'][0][23]
            this.draftYear = newVal['rowSet'][0][27]
            this.draftRound = newVal['rowSet'][0][28]
            this.draftNumber = newVal['rowSet'][0][29]
        }
        
            
    },

}
</script>

<style lang="scss">
    div > span {
        font-weight: bold;
    }
</style>