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
            statIndexDict: {"gp": 0, "gs":1, "min":2, "fgm": 3, "fga":4, "fg_pct": 5, "fg3m": 6, "fg3a":7, "fg3_pct":8, "ftm":9, "fta":10, "ft_pct":11,
                            "oreb":12, "dreb":13, "reb":14, "ast":15, "stl":16, "blk":17, "tov":18, "pf":19, "pts":20}
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
                for (var year in this.comparing[player][seasonIndex]['rowSet']) {
                    years.push(this.comparing[player][seasonIndex]['rowSet'][year][1].slice(0,4))
                    this.comparing[player][seasonIndex]['rowSet'][year].slice(6,27).forEach(function(stat, ind) {
                        stats[ind].push(stat)
                    })
                }
                this.parsedStats[player]['years'] = years
                this.parsedStats[player]['stats'] = stats
            }
        },
        getComparingTraces() {
            let traces = []
            let currentStat = this.statIndexDict[this.stat]
            for (var player in this.comparing) {
                traces.push({
                    x: this.parsedStats[player]['years'],
                    y: this.parsedStats[player]['stats'][currentStat],
                    name: this.comparing[player][0],
                    type: "bar",
                })
            }

            return traces
        },
        drawGraph() {
            this.formatStats()
            var data = this.getComparingTraces()
            var layout = {
                barmode: "group",
                title: `Season ${this.stat.toUpperCase()} Average over Year`,
                xaxis: {
                    tickangle: -45
                }
            }

            var graphDiv = document.getElementById("stats-graph")
            Plotly.react(graphDiv, data, layout)
        }
    },
    watch: {
        comparing: {
            handler: function(newVal) {
                this.drawGraph()
            }
        },
        stat: {
            handler: function(newVal) {
                this.drawGraph()
            }
        },
        regularSeasonBool: {
            handler: function(newVal) {
                this.drawGraph()
            }
        }
    }
}
</script>