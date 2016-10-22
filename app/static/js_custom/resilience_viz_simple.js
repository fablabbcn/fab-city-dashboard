function resilience_viz_simple(id) {

    // Load both regions and countries
    d3.queue()
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/national.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/regional.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/city_gdp.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/city_pop.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/city_surf.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/region_gdp.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/region_pop.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/region_surf.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/country_gdp.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/OECD/country_pop.csv")
        .defer(d3.csv, "../../../static/data_custom/json_stats/WB/country_surf.csv")
        .await(function(error, countries_wellbeing, regions_wellbeing, city_gdp, city_pop, city_surf, region_gdp, region_pop, region_surf, country_gdp, country_pop, country_surf) {
            if (error) {
                console.error('An error loading data: ' + error);
            } else {

                // Colors for the resilience metrics
                var resilience_colors = {
                    "Housing": "#16785D",
                    "Income": "#22357C",
                    "Jobs": "#1A5774",
                    "Community": "#67A61E",
                    "Environment": "#1A9022",
                    "Education": "#551C7B",
                    "Civic engagement": "#7A1676",
                    "Work life balance": "#A81E3E",
                    "Life satisfaction": "#E62339",
                    "Safety": "#B78621",
                    "Health": "#B74021",
                    "Accessibility to services": "#B7B721"
                };

                // Calculate ratio base on GDP / Population
                ratio1 = city_gdp[69]["2012"] / region_gdp[848]["2012"];
                ratio2 = city_pop[69]["2014"] / region_pop[1495]["2014"];
                cire_ratio = (ratio1 + ratio2) / 2;

                // Clean data
                var region_array = [];
                for (var property in regions_wellbeing[283]) {
                    if (property != "Region" && property != "Region Code" && property != "Country") {
                        //region_object[property] = parseFloat(region_data[property]);
                        test = {}
                        test[property] = parseFloat(regions_wellbeing[283][property]);
                        region_array.push(test);
                    }
                }

                var country_array = [];
                for (var property in countries_wellbeing[28]) {
                    if (property != "Country") {
                        //region_object[property] = parseFloat(region_data[property]);
                        test = {}
                        test[property] = parseFloat(countries_wellbeing[28][property]);
                        country_array.push(test);
                    }
                }

                // Calculte the city resilience, in our way
                var city_array = JSON.parse(JSON.stringify(region_array));
                for (property in region_array) {
                    //city_array[property] = region_array[property];
                    for (subproperty in city_array[property]) {
                        city_array[property][subproperty] = city_array[property][subproperty] * cire_ratio;
                    }
                }


                // variables
                var zerox = 0;
                var zeroy = 0;
                var zeroy2 = 10;
                var width = 300;
                var barHeight = 13;
                var space_between_bars = barHeight * 2;
                var space_between_groups = 20;
                var legend_width = 150;

                // Linear scale for scaling the graph
                var linearScale = d3.scaleLinear()
                    .domain([0, 10.0])
                    .range([0, width]);

                // Access svg area
                var svg = d3.select(id)
                    .append("svg")
                    .attr("preserveAspectRatio", "xMaxYMax meet")
                    .attr("viewBox", "0 0 500 600")
                    .classed("svg-content", true);

                // Rounded bars
                var regions = svg.append("g");
                var countries = svg.append("g");
                var cities = svg.append("g");

                var barr = regions.selectAll("g")
                    .data(region_array)
                    .enter()
                    .append("g")

                var barc = countries.selectAll("g")
                    .data(country_array)
                    .enter()
                    .append("g")

                var barci = cities.selectAll("g")
                    .data(city_array)
                    .enter()
                    .append("g")

                // Scale line: city
                barci.append("line")
                    .style("stroke", "#b3b3b3")
                    .attr("x1", zerox + legend_width)
                    .attr("y1", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups) + 6;
                    })
                    .attr("x2", zerox + legend_width + linearScale(10))
                    .attr("y2", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups) + 6;
                    });

                // Scale line: region
                barr.append("line")
                    .style("stroke", "#b3b3b3")
                    .style("opacity", 0.4)
                    .attr("x1", function(d) {
                        for (property in d) {
                            var resilience_value = d[property];
                        }
                        return zerox + legend_width;
                    })
                    .attr("y1", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups) + 6 + barHeight;
                    })
                    .attr("x2", zerox + legend_width + linearScale(10))
                    .attr("y2", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups) + 6 + barHeight;
                    });

                // Scale line: country
                barc.append("line")
                    .style("stroke", "#b3b3b3")
                    .style("opacity", 0.2)
                    .attr("x1", function(d) {
                        for (property in d) {
                            var resilience_value = d[property];
                        }
                        return zerox + legend_width;
                    })
                    .attr("y1", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups) + 6 + barHeight * 2;
                    })
                    .attr("x2", zerox + legend_width + width)
                    .attr("y2", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups) + 6 + barHeight * 2;
                    });

                // The bars: region
                barr.append("rect")
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "region " + property.toLowerCase() + " bar";
                    })
                    .style("opacity", 0.4)
                    .attr("x", zerox + legend_width)
                    .attr("y", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups) + barHeight;
                    })
                    .attr("width", function(d) {
                        for (property in d) {
                            var resilience_value = d[property];
                        }
                        return linearScale(resilience_value);
                    })
                    .attr("height", barHeight)
                    .attr("rx", 6)
                    .attr("ry", 6)
                    .attr("fill", function(d) {
                        for (property in d) {
                            var the_color = resilience_colors[property];
                        }
                        return the_color;
                    });

                // The legend labels: region
                barr.append("text")
                    .style("opacity", 0.4)
                    .attr("x", zerox)
                    .attr("y", function(d, i) {
                        return zeroy + 6 + i * (space_between_bars + space_between_groups) + barHeight;
                    })
                    .attr("dy", ".35em")
                    .text("Value at regional level");

                // The legend labels: cities
                barci.append("text")
                    .attr("x", zerox)
                    .attr("y", function(d, i) {
                        return zeroy + 6 + i * (space_between_bars + space_between_groups);
                    })
                    .attr("dy", ".35em")
                    .text(function(d) {
                        for (property in d) {
                            var label_text = property;
                        }
                        return label_text + " ";
                    });

                // The legend labels: country
                barc.append("text")
                    .style("opacity", 0.2)
                    .attr("x", zerox)
                    .attr("y", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups) + 6 + barHeight * 2;
                    })
                    .attr("dy", ".35em")
                    .text("Value at country level");

                // The value labels: region
                barr.append("text")
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "region " + property.toLowerCase() + " value";
                    })
                    .style("opacity", 0.4)
                    .text(function(d) {
                        for (property in d) {
                            var label_value = d[property];
                        }
                        return label_value + "/10";
                    })
                    .attr("x", zerox + legend_width + width + zerox + zeroy2)
                    .attr("y", function(d, i) {
                        return zeroy2 + i * (space_between_bars + space_between_groups) + barHeight;
                    });

                // The value labels: cities
                barci.append("text")
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
                        return Math.round(label_value * 10) / 10 + "/10";
                    })
                    .attr("x", zerox + legend_width + width + zerox + zeroy2)
                    .attr("y", function(d, i) {
                        return zeroy2 + i * (space_between_bars + space_between_groups)
                    });

                // The value labels: countries
                barc.append("text")
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "countries " + property.toLowerCase() + " value";
                    })
                    .style("opacity", 0.2)
                    .text(function(d) {
                        for (property in d) {
                            var label_value = d[property];
                        }
                        return Math.round(label_value * 10) / 10 + "/10";
                    })
                    .attr("x", zerox + legend_width + width + zerox + zeroy2)
                    .attr("y", function(d, i) {
                        return zeroy2 + i * (space_between_bars + space_between_groups) + 6 + barHeight + 6;
                    });

                // The bars: city
                barci.append("rect")
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "city " + property.toLowerCase() + " bar";
                    })
                    .attr("x", zerox + legend_width)
                    .attr("y", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups);
                    })
                    .attr("width", function(d) {
                        for (property in d) {
                            var resilience_value = d[property];
                        }
                        return linearScale(resilience_value);
                    })
                    .attr("height", barHeight)
                    .attr("rx", 6)
                    .attr("ry", 6)
                    .attr("fill", function(d) {
                        for (property in d) {
                            var the_color = resilience_colors[property];
                        }
                        return the_color;
                    });

                // The bars: country
                barc.append("rect")
                    .style("opacity", 0.1)
                    .attr("class", function(d) {
                        for (property in d) {
                            var the_class = property;
                        }
                        return "country " + property.toLowerCase() + " bar";
                    })
                    .attr("x", zerox + legend_width)
                    .attr("y", function(d, i) {
                        return zeroy + i * (space_between_bars + space_between_groups) + space_between_bars / 2 + barHeight;
                    })
                    .attr("width", function(d) {
                        for (property in d) {
                            var resilience_value = d[property];
                        }
                        return linearScale(resilience_value);
                    })
                    .attr("height", barHeight)
                    .attr("rx", 6)
                    .attr("ry", 6)
                    .attr("fill", function(d) {
                        for (property in d) {
                            var the_color = resilience_colors[property];
                        }
                        return the_color;
                    });

                // SVG icons
                var accessibility_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/accesibility_to_services_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    accessibility_icon.node().appendChild(xml.documentElement);
                });

                var civic_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/civic_engagement_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    civic_icon.node().appendChild(xml.documentElement);
                });

                var community_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/community_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    community_icon.node().appendChild(xml.documentElement);
                });

                var education_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/education_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    education_icon.node().appendChild(xml.documentElement);
                });

                var environment_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/environment_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    environment_icon.node().appendChild(xml.documentElement);
                });

                var health_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/health_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    health_icon.node().appendChild(xml.documentElement);
                });

                var housing_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/housing_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    housing_icon.node().appendChild(xml.documentElement);
                });

                var income_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/income_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    income_icon.node().appendChild(xml.documentElement);
                });

                var jobs_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/jobs_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    jobs_icon.node().appendChild(xml.documentElement);
                });

                var life_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/life_satisfaction_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    life_icon.node().appendChild(xml.documentElement);
                });

                var safety_icon = svg.append("g");
                d3.xml("../../../static/images/icons/svg/safety_cr.svg").mimeType("image/svg+xml").get(function(error, xml) {
                    if (error) throw error;
                    safety_icon.node().appendChild(xml.documentElement);
                });

                // SVG icons transformations
                var icon_scale = 0.03;
                var icon_x = legend_width - 20;
                var icon_y = barHeight - 2;

                education_icon.attr("transform", "translate (" + icon_x + ", " + icon_y + ") scale(" + icon_scale + ")");
                icon_y = icon_y + space_between_bars + space_between_groups;
                jobs_icon.attr("transform", "translate (" + icon_x +
                    ", " + icon_y + ") scale(" +
                    icon_scale + ")");
                icon_y = icon_y + space_between_bars + space_between_groups;
                income_icon.attr("transform", "translate (" + icon_x + ", " + icon_y + ") scale(" + icon_scale + ")");
                icon_y = icon_y +
                    space_between_bars + space_between_groups;
                safety_icon.attr(
                    "transform", "translate (" + icon_x + ", " + icon_y + ") scale(" + icon_scale + ")");
                icon_y = icon_y + space_between_bars + space_between_groups;
                health_icon.attr("transform", "translate (" + icon_x + ", " + icon_y +
                    ") scale(" + icon_scale +
                    ")");
                icon_y = icon_y + space_between_bars + space_between_groups;
                environment_icon.attr("transform", "translate (" + icon_x + ", " + icon_y + ") scale(" + icon_scale + ")");
                icon_y = icon_y + space_between_bars +
                    space_between_groups;
                civic_icon.attr("transform",
                    "translate (" + icon_x + ", " + icon_y + ") scale(" + icon_scale + ")");
                icon_y = icon_y + space_between_bars + space_between_groups;
                accessibility_icon.attr("transform", "translate (" + icon_x + ", " + icon_y +
                    ") scale(" + icon_scale + ")");
                icon_y = icon_y + space_between_bars + space_between_groups;
                housing_icon.attr("transform", "translate (" + icon_x + ", " + icon_y + ") scale(" + icon_scale + ")");
                icon_y = icon_y +
                    space_between_bars + space_between_groups;
                community_icon.attr("transform", "translate (" +
                    icon_x + ", " + icon_y + ") scale(" + icon_scale + ")");
                icon_y = icon_y + space_between_bars + space_between_groups;
                life_icon.attr("transform", "translate (" + icon_x + ", " + icon_y + ") scale(" + icon_scale + ")");

            }
        });

}
