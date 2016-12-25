var map;
var geocoder;
var service;
var infowindow;
var marker;
function initMap() {
    var mapProp = {
        center: new google.maps.LatLng(30.267, -97.743),
        zoom: 10,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        styles: [{featureType: "poi", elementType: "labels", stylers: [{visibility: "off"}]}]
    };
    ///////////////////////////////////////////////////////////////
    // INTIALIZE MAP COMPONENTS
    ///////////////////////////////////////////////////////////////
    map = new google.maps.Map($('#googleMap')[0], mapProp);
    geocoder = new google.maps.Geocoder();
    service = new google.maps.places.PlacesService(map);
    infowindow = new google.maps.InfoWindow();
    marker = new google.maps.Marker({
        map: map
    });
    // add search bar
    var input = /** @type {!HTMLInuputElement} */($('#pac-input')[0]);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);
    ///////////////////////////////////////////////////////////////
    // ADD EVENT LISTENERS
    ///////////////////////////////////////////////////////////////

    // add event listener for click event
    google.maps.event.addListener(map, 'click', function (event) {
        replaceMarkerByLatLng(event.latLng);

        reverseGeocodeAddress(event.latLng);
        $('#latLng').val(event.latLng);
    });

    // add event listener for search event
    autocomplete.addListener('place_changed', function () {
        var place = autocomplete.getPlace();
        replaceMarkerByPlace(place);

        geocodeAddress(place.formatted_address);
        $('#latLng').val(place.geometry.location);
    })
}

///////////////////////////////////////////////////////////////
// MARKER REPLACEMENT
///////////////////////////////////////////////////////////////
function replaceMarkerByPlace(place) {
    infowindow.close();
    marker.setVisible(false);
    if (!place.geometry) {
        window.alert('Unable to find that address');
        return;
    }
    if (place.geometry.viewport) {
        map.fitBounds(place.geometry.viewport);
    }
    else {
        map.setCenter(place.geometry.location);
        map.setZoom(10);
    }
    marker.setIcon(/** @type {google.maps.Icon} */({
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(35, 35)
    }));
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);
    var address = '';
    if (place.formatted_address) {
        address = place.formatted_address;
    }
    infowindow.setContent(place.name);
    infowindow.open(map, marker);
}

function replaceMarkerByLatLng(latlng) {
    infowindow.close();
    marker.setVisible(false);
    map.setCenter(latlng);
    marker.setPosition(latlng);
    marker.setVisible(true);
}

///////////////////////////////////////////////////////////////
// GEOCODING FUNCTIONS
///////////////////////////////////////////////////////////////
function geocodeAddress(address) {
    var city, state, i;
    geocoder.geocode({'address': address}, function (results, status) {
        if (status == 'OK') {
            for (i = 0; i < results[0]['address_components'].length; i++) {
                var types = results[0]['address_components'][i]['types'];
                if (types[0] == 'locality' && types[1] == 'political') {
                    city = results[0]['address_components'][i]['long_name'];
                }
                else if (types[0] == 'administrative_area_level_1') {
                    state = results[0]['address_components'][i]['long_name'];
                }
            }
            $('#location_desc').val(city.concat(', ').concat(state));
        } else {
            console.log('Geocode was not successful for the following reason: ' + status);
            $('#location_desc').text('Unable to determine address');
        }
    });
}

function reverseGeocodeAddress(latlng) {
    var city, state, i;
    geocoder.geocode({'location': latlng}, function (results, status) {
        if (status == 'OK') {
            for (i = 0; i < results[0]['address_components'].length; i++) {
                var types = results[0]['address_components'][i]['types'];
                if (types[0] == 'locality' && types[1] == 'political') {
                    city = results[0]['address_components'][i]['long_name'];
                }
                else if (types[0] == 'administrative_area_level_1') {
                    state = results[0]['address_components'][i]['long_name'];
                }
            }
            $('#location_desc').val(city.concat(', ').concat(state));
        }
        else {
            console.log('Geocode was not successful for the following reason: ' + status);
            $('#location_desc').text('Unable to determine address');
        }
    });
}
