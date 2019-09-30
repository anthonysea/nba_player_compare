<template>
    <div id="player-career-summary">
        <div id="reg-season-totals">
            <span>Regular Season Totals</span>
            <table v-if="careerTotalsReg">
            <thead>
            <tr>
                <td v-for="col in careerTotalsReg['headers'].slice(3, 24)">{{ col }}</td>
            </tr>
            </thead>
            <tr>
                <td v-for="col in careerTotalsReg['rowSet'][0].slice(3,24)">{{ col }}</td>
            </tr>
            </table>
        </div>

        <div id="post-season-totals">
            <span>Post Season Totals</span>
            <table v-if="careerTotalsPost">
            <thead>
            <tr>
                <td v-for="col in careerTotalsPost['headers'].slice(3, 24)">{{ col }}</td>
            </tr>
            </thead>
            <tr>
                <td v-for="col in careerTotalsPost['rowSet'][0].slice(3,24)">{{ col }}</td>
            </tr>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    props: ["careerStats",],
    data() {
        return {
            seasonTotalsReg: null,
            careerTotalsReg: null,
            seasonTotalsPost: null,
            careerTotalsPost: null,
        }
    },
    watch: {
        careerStats: {
            immediate: true,
            handler: function(newVal, oldVal) {
                this.seasonTotalsReg = newVal[0]['rowSet']
                this.careerTotalsReg = newVal[1]
                this.seasonTotalsPost = newVal[2]['rowSet']
                this.careerTotalsPost = newVal[3]
            }
        }
    }
}
</script>

<style lang="scss">

    #player-career-summary {
        margin-top: 1em;
    }

    #player-career-summary span {
        font-style: italic;
    }
    #player-career-summary  thead {
        color: #006ac7;
    }
</style>