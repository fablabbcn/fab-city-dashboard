function city_region_country_viz(id) {
    // Load both regions and countries
    d3.queue()
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/city_gdp.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/city_pop.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/city_surf.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/region_gdp.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/region_pop.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/region_surf.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/country_gdp.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/country_pop.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/WB/country_surf.csv")
        .await(function(error, city_gdp, city_pop, city_surf, region_gdp, region_pop, region_surf, country_gdp, country_pop, country_surf) {
            if (error) {
                console.error('An error loading data: ' + error);
            } else {



                var gdp = [{
                    "City GDP": city_gdp[69]["2012"]
                }, {
                    "Region GDP": region_gdp[848]["2012"]
                }, {
                    "Country GDP": country_gdp[24]["2015"]
                }];
                var pop = [{
                    "City population": city_pop[69]["2014"]
                }, {
                    "Region population": region_pop[1495]["2014"]
                }, {
                    "Country population": country_pop[28]["2011"]
                }];
                var surf = [{
                    "City surface": city_surf[69]["2014"]
                }, {
                    "Region surface": region_surf[1457]["2014"]
                }, {
                    "Country surface": country_surf[178]["2015"]
                }];

                // variables
                var zerox = 0;
                var zeroy = 5;
                var zeroy2 = 10;
                var width = 300;
                var barHeight = 13;
                var space_between_bars = barHeight * 2;
                var space_between_groups = 20;
                var legend_width = 120;

                // Linear scale for gdp
                var gdpScale = d3.scaleLinear()
                    .domain([0, country_gdp[24]["2015"]])
                    .range([0, width]);

                var popScale = d3.scaleLinear()
                    .domain([0, country_pop[28]["2011"]])
                    .range([0, width]);

                var surfScale = d3.scaleLinear()
                    .domain([0, country_surf[178]["2015"]])
                    .range([0, width]);

                // Access svg area
                var svg = d3.select(id)
                    .append("svg")
                    .attr("preserveAspectRatio", "xMinYMin meet")
                    .attr("viewBox", "0 0 600 200")
                    .classed("svg-content", true);

                // Rounded bars
                var gdp_g = svg.append("g");
                var pop_g = svg.append("g");
                var surf_g = svg.append("g");

                var barg = gdp_g.selectAll("g")
                    .data(gdp)
                    .enter()
                    .append("g")
                    .attr("transform", "translate(0, " + zeroy + ")");

                var barp = pop_g.selectAll("g")
                    .data(pop)
                    .enter()
                    .append("g")
                    .attr("transform", "translate(0, " + (zeroy + 60) + ")");

                var bars = surf_g.selectAll("g")
                    .data(surf)
                    .enter()
                    .append("g")
                    .attr("transform", "translate(0, " + (zeroy + 120) + ")");

                // Scale line: gdp
                barg.append("line")
                    .style("stroke", "#b3b3b3")
                    .attr("x1", zerox + legend_width)
                    .attr("y1", function(d, i) {
                        return zeroy + i * barHeight;
                    })
                    .attr("x2", zerox + legend_width + width)
                    .attr("y2", function(d, i) {
                        return zeroy + i * barHeight;
                    });

                // The legend labels: gdp
                barg.append("text")
                    .attr("x", zerox)
                    .attr("y", function(d, i) {
                        return zeroy + i * barHeight;
                    })
                    .attr("dy", ".35em")
                    .text(function(d) {
                        for (property in d) {
                            var label_text = property;
                        }
                        return label_text + " ";
                    });

                // The value labels: gdp
                barg.append("text")
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "city " + property.toLowerCase() + " value";
                    })
                    .text(function(d) {
                        for (property in d) {
                            var label_value = d[property];
                        }
                        return Intl.NumberFormat().format(Math.round(label_value * 10) / 10) + " $ (millions)";
                    })
                    .attr("x", zerox + legend_width + width + zerox + zeroy2)
                    .attr("y", function(d, i) {
                        return zeroy + i * barHeight + 6;
                    });

                // The bars: gdp
                barg.append("rect")
                    .style("opacity", 0.4)
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "city " + property.toLowerCase() + " bar";
                    })
                    .attr("x", zerox + legend_width)
                    .attr("y", function(d, i) {
                        return zeroy - barHeight / 2 + i * barHeight;
                    })
                    .attr("width", function(d) {
                        for (property in d) {
                            return gdpScale(d[property]);
                        }
                    })
                    .attr("height", barHeight)
                    .attr("rx", 6)
                    .attr("ry", 6)
                    .attr("fill", "#000");


                // Population

                // Scale line
                barp.append("line")
                    .style("stroke", "#b3b3b3")
                    .attr("x1", zerox + legend_width)
                    .attr("y1", function(d, i) {
                        return zeroy + i * barHeight;
                    })
                    .attr("x2", zerox + legend_width + width)
                    .attr("y2", function(d, i) {
                        return zeroy + i * barHeight;
                    });

                // The legend labels
                barp.append("text")
                    .attr("x", zerox)
                    .attr("y", function(d, i) {
                        return zeroy + i * barHeight;
                    })
                    .attr("dy", ".35em")
                    .text(function(d) {
                        for (property in d) {
                            var label_text = property;
                        }
                        return label_text + " ";
                    });

                // The value labels
                barp.append("text")
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "city " + property.toLowerCase() + " value";
                    })
                    .text(function(d) {
                        for (property in d) {
                            var label_value = d[property];
                        }
                        return Intl.NumberFormat().format(Math.round(label_value * 10) / 10) + " persons";
                    })
                    .attr("x", zerox + legend_width + width + zerox + zeroy2)
                    .attr("y", function(d, i) {
                        return zeroy + i * barHeight + 6;
                    });

                // The bars
                barp.append("rect")
                    .style("opacity", 0.4)
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "city " + property.toLowerCase() + " bar";
                    })
                    .attr("x", zerox + legend_width)
                    .attr("y", function(d, i) {
                        return zeroy - barHeight / 2 + i * barHeight;
                    })
                    .attr("width", function(d) {
                        for (property in d) {
                            return popScale(d[property]);
                        }
                    })
                    .attr("height", barHeight)
                    .attr("rx", 6)
                    .attr("ry", 6)
                    .attr("fill", "#000");

                // Surface

                // Scale line
                bars.append("line")
                    .style("stroke", "#b3b3b3")
                    .attr("x1", zerox + legend_width)
                    .attr("y1", function(d, i) {
                        return zeroy + i * barHeight;
                    })
                    .attr("x2", zerox + legend_width + width)
                    .attr("y2", function(d, i) {
                        return zeroy + i * barHeight;
                    });

                // The legend labels
                bars.append("text")
                    .attr("x", zerox)
                    .attr("y", function(d, i) {
                        return zeroy + i * barHeight;
                    })
                    .attr("dy", ".35em")
                    .text(function(d) {
                        for (property in d) {
                            var label_text = property;
                        }
                        return label_text + " ";
                    });

                // The value labels
                bars.append("text")
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "city " + property.toLowerCase() + " value";
                    })
                    .text(function(d) {
                        for (property in d) {
                            var label_value = d[property];
                        }
                        return Intl.NumberFormat().format(Math.round(label_value * 10) / 10) + " Km2";
                    })
                    .attr("x", zerox + legend_width + width + zerox + zeroy2)
                    .attr("y", function(d, i) {
                        return zeroy + i * barHeight + 6;
                    });

                // The bars
                bars.append("rect")
                    .style("opacity", 0.4)
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "city " + property.toLowerCase() + " bar";
                    })
                    .attr("x", zerox + legend_width)
                    .attr("y", function(d, i) {
                        return zeroy - barHeight / 2 + i * barHeight;
                    })
                    .attr("width", function(d) {
                        for (property in d) {
                            return surfScale(d[property]);
                        }
                    })
                    .attr("height", barHeight)
                    .attr("rx", 6)
                    .attr("ry", 6)
                    .attr("fill", "#000");

            }
        });
}
