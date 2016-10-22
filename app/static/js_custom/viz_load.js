function viz_load(d) {

    // Select elements of the interface
    var title = d3.select('#title');
    var viz = d3.select('#wholeviz');
    var city = d3.select('#city');
    var region = d3.select('#region');
    var country = d3.select('#country');
    var description = d3.select('#description');
    var content = d3.select('#content');

    // Update the interface with the select Fab City
    title.html(d.name);
    city.html(d.city);
    region.html(d.region);
    country.html(d.country);
    description.html(d.description);

    // Load the visualizations
    city_region_country_viz("div#city-region-country");
    resilience_viz_simple("div#resilience-city");
    labs_map(d);
    resilience_project_viz();

}
