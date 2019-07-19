function initMap(){
  // Map options

  var options = {
    zoom:12 ,
    center:{lat:37.4323,lng:-121.8996}
  }
  // New map
  var map = new google.maps.Map(document.getElementById('map'), options);

  // get gym data from html in the form of json object
  var gymData = $('#gym-data').data();


  markers=[]
  gyms = gymData['name']

  // loops through gym json object and appends name, coords, address to markers array
  for (var i in gyms){
    if (gyms.hasOwnProperty(i))

      // push to markers array so we can iterate through the array
      markers.push({
        name: i,
        coords: gyms[i]['geocode'],
        address: gyms[i]['address'],
        place_id: gyms[i]['place_id'],
      })
  }

  for (var i = 0; i < markers.length; i++) {
    addMarker(markers[i]);
  }

// function to add place marker for gyms
  function addMarker(props){
    var marker = new google.maps.Marker({
      position: props.coords,
      map:map,
    });

    // adds a link to the gym's info page
    var infoWindow = new google.maps.InfoWindow({
      content: '<a href="/gym/' + props.place_id + '">' + props.name + '</a>' +
        '<p>' + props.address + '</p>'
    });

    // on click, opens a window
    marker.addListener('click', function(){
    infoWindow.open(map, marker);
      });
    }
}
