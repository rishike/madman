
<template>
	<div class="columns">
	<div class="column is-one-third buttons" style="height: 800px;overflow-y: scroll; overflow-x:scroll;">
		<h1 class="title has-text-centered"> Attractions</h1>
		<div :class="attractionClass" v-html="mapLocationListEl">
			
		</div>
	</div>
	<div id="mapdiv" class="column" ref="mapElement">
	</div>
</div>
</template>

  	


<script type="text/javascript">
import * as L from "leaflet" ;
import "leaflet-ajax";



export default {
		data: function () {
			return {
				mymap:"",
				geojsonlayer:"",
				attractionClass:"has-text-centered ",
				mapLocationListEl:""

			}
		},
		methods: {
			zoomMap: function() { 
				this.mymap.setView([28.60287,77.32948], 17);
			}
		},
		mounted() {
			const $this=this;
    		this.mymap = L.map(this.$refs['mapElement']).setView([28.60287,77.32948], 13);
    		L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(this.mymap);

	// L.marker([28.60287,77.32948]).addTo(this.mymap)
	//     .bindPopup('New Delhi')
	//     .openPopup();
		this.geojsonlayer = new L.GeoJSON.AJAX('geojson/', {

					pointToLayer: function(feature, latlng) {
					const str = `<div>
					<button id="zoomTo${feature.properties.name.replace(/ /g,'')}" class="button is-primary"> ${feature.properties.name}</button></div>
					`;

					
					
					$this.mapLocationListEl += str;


					const newStr =`<h4>${feature.properties.name}</h4><hr>
					<a href='${feature.properties.web}' target="blank">
					<img src='/static/img/${feature.properties.image}' width='200px'/>
					</a>`;

					$this.$nextTick(function () {
					   	document.getElementById(`zoomTo${feature.properties.name.replace(/ /g,'')}`).addEventListener("click", function(){
							$this.mymap.setView([latlng.lat, latlng.lng],17)		  
						}); 
					});
				
					return L.marker(latlng).bindPopup(newStr);

				}
		});

		this.geojsonlayer.addTo(this.mymap);

	
		this.mymap.addEventListener('mousemove',e => {
			const str = "Latitude: "+ e.latlng.lat.toFixed(5)+ " Longitude: "+ e.latlng.lng.toFixed(5)+ " Zoom Level: "+ this.mymap.getZoom();
			document.getElementById('map_coords').innerHTML = str;

		});

		
    
  	}
  
};
</script>