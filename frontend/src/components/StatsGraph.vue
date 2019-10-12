<template>
    <div id="graph">
        
    </div>
</template>

<script>
import Plotly from "plotly.js-dist"

export default {
    props: ["comparing", // Object of all the players to compare and their stats
            "stat", // The stat to graph
            "regularSeasonBool"], // Boolean to indicate weather if graph is for regular season or post season
    data() {
        return {
            parsedStats: {}, // Object containing each player and their corresponding stats for the current selection of stat-type and regular-season-bool
        }
    },
    methods: {
        formatStats() {
            var seasonIndex = this.regularSeasonBool ? 1 : 3
            for (var player in this.comparing) {
                this.parsedStats[player] = {}
                var years = []
                var stats = []
                for (var i = 0; i < 21; i++) {
                    stats[i] = []
                } 
                console.log(stats)
                for (var year in this.comparing[player][seasonIndex]['rowSet']) {
                    years.push(this.comparing[player][seasonIndex]['rowSet'][year][1])
                    this.comparing[player][seasonIndex]['rowSet'][year].slice(6,27).forEach(function(stat, ind) {
                        stats[ind].push(stat)
                    })
                }
                this.parsedStats[player]['years'] = years
                this.parsedStats[player]['stats'] = stats
            }
            console.log(this.parsedStats)
        }
    },
    watch: {
        comparing: {
            handler: function(newVal) {
                this.formatStats()
                var graphDiv = document.getElementById("stats-graph")
                console.log(graphDiv)
                Plotly.newPlot(graphDiv, [{
                    x: [1,2, 3, 4],
                    y: [2, 4, 6, 8],
                    type: "bar",
                }])
            }
        }
    }
}
</script>