function viz_load(d) {
    console.log("viz loada");
    var title = d3.select('#title');
    var viz = d3.select('#wholeviz');
    var city = d3.select('#city');
    var region = d3.select('#region');
    var country = d3.select('#country');
    var description = d3.select('#description');
    var content = d3.select('#content');
    title.html(d.name);
}
