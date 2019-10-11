<template>
    <div id="graph">
        
    </div>
</template>

<script>
import Plotly from "plotly.js-dist"

export default {
    props: ["comparing", // Object of all the players to compare and their stats
            "stat", // The stat to graph
            "regular-season"], // Boolean to indicate weather if graph is for regular season or post season
    methods: {

    }
}
</script>