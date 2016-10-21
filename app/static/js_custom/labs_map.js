function labs_map(d) {

    // initialize the map
    var map = L.map('map_labs').setView([d.lat, d.long], 10);

    // load a tile layer
    var basemap = L.tileLayer('http://tile.stamen.com/toner-lite/{z}/{x}/{y}.png', {
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
    }).addTo(map);

    // Functional urban areas plotting
    var fua_geojson = new L.GeoJSON.AJAX('../../../static/data_custom/geojson_basemaps/regions/ESP/ESP_MAs_2016.geojson', {
        style: function(feature) {
            switch (feature.properties.CORE) {
                case 0:
                    return {
                        color: "#8f7e6f",
                        weight: 1,
                        opacity: 0.55,
                        fillColor: "#8f7e6f",
                        fillOpacity: 0.25
                    };
                case 1:
                    return {
                        color: "#5d3d1e",
                        weight: 2,
                        opacity: 1,
                        fillColor: "#5d3d1e",
                        fillOpacity: 0.35
                    };
            }
        }
    }).addTo(map);

    var fablabs_layer = new L.layerGroup();

    var fablabIcon = L.icon({
        iconUrl: '../../../static/images/icons/svg/fablabs-red.png',
        iconSize: [25, 25]
    });

    function onEachMarker(feature, layer) {
        var props = feature.properties;
        var popupContent = "<p></p>";
        if (props && props.name) {
            popupContent += '<h5>' + props.name + '</h5> ( ' + props.lab_type + ' )' + '<hr>' +
                '<p style="margin-left: 15px"><em>city</em> : ' + props.city + ' ( ' + props.country_code + ' )' +
                '<br><em>address</em> : ' + props.address_1 +
                '</p>';
        }
        layer.bindPopup(popupContent);
    }

    var geojsonFeature = new L.GeoJSON.AJAX('../../../static/data_custom/geojson_labs/labs.geojson', {
        onEachFeature: onEachMarker,
        pointToLayer: function(feature, latlng) {
            // GeoJSON coordinates and Leaflet coordinates are inverted
            // But GeoJSON is a standard, so:
            // Solution from here: https://github.com/mapbox/geojson.io/issues/289
            var latlngNew = $.extend(true, {}, latlng);
            latlngNew.lat = latlng.lng;
            latlngNew.lng = latlng.lat;
            return L.marker(latlngNew, {
                icon: fablabIcon
            });
        }
    }).addTo(map);

    var regionStyle = {
        "color": "#c38c5c",
        "weight": 1,
        "fillColor": "#c38c5c",
        "fillOpacity": 0.15
    };

    var region_geojson = new L.GeoJSON.AJAX('../../../static/data_custom/geojson_basemaps/regions/ESP/ESP_admin_level_4.geojson', regionStyle).addTo(map);

}
