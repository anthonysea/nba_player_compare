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
        <!-- <tr v-for="player in careerStatsRS" :key="player.id">
            <td id="table-heading">{{ player[0] }}</td>
            <td v-for="stat in cleanStatLine(player.slice(1,22))" :key="stat.id">{{ stat }}</td>
        </tr> -->
            <tr v-for="player in comparing" :key="player.id">
            <!-- Get the name of the player -->
            <td id="table-heading">{{ player[0] }}</td>
            <!-- Get the array that contains the regular season career totals -->
            <td v-for="stat in cleanStatLine(player[2]['rowSet'][0]).slice(3,24)" :key="stat.id">{{ stat }}</td>
        </tr>
    </table>
    <p>Career Totals (Post Season)</p>
    <table>
        <thead>
        <tr>
            <td></td>
            <td id="table-heading" v-for="heading in headers" :key="heading.id">{{ heading }}</td>
        </tr>
        </thead>
        <tr v-for="player in comparing" :key="player.id">
            <!-- Get the name of the player -->
            <td id="table-heading">{{ player[0] }}</td>
            <!-- Get the array that contains the post season career totals -->
            <td v-for="stat in cleanStatLine(player[4]['rowSet'][0]).slice(3,24)" :key="stat.id">{{ stat }}</td>
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
            // careerStatsRS: {},
            // careerStatsPS: {},
        }
    },
    watch: {
        comparing: {
            immediate: true,
            handler: function(newVal, oldVal) {
                
                if (!newVal) {
                    return 
                }
                // Only update headers object once
                if (Object.keys(this.headers).length === 0 && this.headers.constructor === Object) {
                    this.headers = newVal[Object.keys(newVal)[0]][2]['headers'].slice(3,24)
                    this.headers[5] = "FG%"
                    this.headers[8] = "FG3%"
                    this.headers[11] = "FT%"
                }

                
                // for (var ele in newVal) {
                //     console.log(newVal[ele])

                //     this.$set(this.careerStatsRS, ele, newVal[ele][2]['rowSet'][0].slice(3,24))
                //     // Set first element in array to be the name of the player
                //     this.careerStatsRS[ele].unshift(newVal[ele][0])
                    
                //     this.$set(this.careerStatsPS, ele, newVal[ele][4]['rowSet'][0].slice(3,24))
                //     // Set first element in array to be the name of the player
                //     this.careerStatsPS[ele].unshift(newVal[ele][0])
                // }

                
            }
        }
    },
    methods: {
        cleanStatLine(arr) {
            // If the rowset in the data does not exist -> fill with dashes
            if (arr === undefined || (arr.length == 0)) {
                arr = []
                for (var i = 0; i < 24; i++) {
                    arr.push("-")
                }
                return arr 
            }

            // Filter to remove null values in statline
            const copy = []
            arr.forEach(function(ele) {
                if (ele === null || (ele === undefined)) {
                    copy.push("-")
                } else {
                    copy.push(ele)
                }
            })
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

