<template>
<div id="career-stats">
    <p>Career Totals (Regular Season)</p>
    <table>
        <thead>
        <tr>
            <td></td>
            <td id="table-heading" v-for="heading in headers" :key="heading.id">{{ heading }}</td>
        </tr>
        </thead>
        <tr v-for="(player, rowSet, ind) in comparing" :key="player.id">
            <td id="table-heading">{{ playerNames[ind] }}</td>
            <td v-for="stat in player[1]['rowSet'][0].slice(3,24)" :key="stat.id">{{ stat }}</td>
        </tr>
    </table>
    <p>Career Totals - Post Season</p>
    <table>
        <thead>
        <tr>
            <td></td>
            <td id="table-heading" v-for="heading in headers" :key="heading.id">{{ heading }}</td>
        </tr>
        </thead>
        <tr v-for="(player, rowSet, ind) in comparing" :key="player.id">
            <td id="table-heading">{{ playerNames[ind] }}</td>
            <td v-for="stat in player[3]['rowSet'][0].slice(3,24)" :key="stat.id">{{ stat }}</td>
        </tr>
    </table>
</div>
</template>

<script>
export default {
    props: ["comparing",],
    data() {
        return {
            headers: {},
            heading: "",
            player: [],
            stat: "",
            playerNames: [],
        }
    },
    watch: {
        comparing: {
            immediate: true,
            handler: function(newVal) {
                if (!newVal) {
                    return
                }
                this.headers = newVal[Object.keys(newVal)[0]][1]['headers'].slice(3,24)
            }
        }
    },
    created() {
        this.$root.$on('updateCurrentPlayer', player => {
            this.playerNames.push(player)
        })
    }
}
</script>

<style lang="scss">
#career-stats {
    margin-top: 2em;
}

#career-stats p {
    font-weight: bold;
}

#career-stats #table-heading {
    color: rgb(0, 99, 90);
    font-weight: bold;
}

</style>

