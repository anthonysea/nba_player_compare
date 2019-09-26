<template>
    <div>
        <span v-for="item in this.$data"> {{ item }}</span>
        
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