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
        <tr v-for="player in careerStatsRS" :key="player.id">
            <td id="table-heading">{{ player[0] }}</td>
            <td v-for="stat in cleanStatLine(player.slice(1,22))" :key="stat.id">{{ stat }}</td>
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
        <tr v-for="player in careerStatsPS" :key="player.id">
            <td id="table-heading">{{ player[0] }}</td>
            <td v-for="stat in cleanStatLine(player.slice(1,22))" :key="stat.id">{{ stat }}</td>
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
            careerStatsRS: {},
            careerStatsPS: {},
        }
    },
    watch: {
        comparing: {
            immediate: true,
            handler: function(newVal) {
                if (!newVal) {
                    return
                }
                // console.log(JSON.stringify(newVal))
                this.headers = newVal[Object.keys(newVal)[0]][2]['headers'].slice(3,24)

                for(var ele in newVal) {
                    console.log(newVal[ele])
                    this.$set(this.careerStatsRS, ele, newVal[ele][2]['rowSet'][0].slice(3,24))
                    this.careerStatsRS[ele].unshift(newVal[ele][0])
                    
                    this.$set(this.careerStatsPS, ele, newVal[ele][4]['rowSet'][0].slice(3,24))
                    this.careerStatsPS[ele].unshift(newVal[ele][0])
                }
            }
        }
    },
    methods: {
        cleanStatLine(arr) {
            // Filter to remove null values in statline
            const copy = []
            arr.forEach(function(ele) {
                if (ele === null) {
                    copy.push("-")
                } else {
                    copy.push(ele)
                }
            })
            console.log(copy)
            return copy
        }
    },
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

