
<template>
	<div class="columns">

	<div class="column is-4 buttons" style="overflow-y: scroll;">
		
		<!-- <h1 class="title has-text-centered"> Attractions</h1> -->
		<!-- <div><button id="btnBuffer" class="button is-warning">Buffer</button></div> -->

		<div :class="attractionClass">
			<button class="button">Download CSV</button>
			<button class="button">Download Xls</button>
			<button class="button">Download PDF</button>
			<button class="button">Download PNG</button>
		</div>
	</div>
	<div id="mapdiv" class="column is-8" ref="mapElement" v-on:dblclick="show()">
	</div>

	
	<mapmodal :isActive="isActive" :lngVal="lngVal" :latVal="latVal"  @isActiveEvt="customEventFun"></mapmodal>


</div>
</div>
</template>


<script type="text/javascript">
import * as L from "leaflet" ;
import "leaflet-ajax";
import mapmodal from "./MapModal.vue";



export default {
		data: function () {
			return {
				mymap:"",
				geojsonlayer:"",
				attractionClass:"has-text-centered side",
				bufferLayer:"",
				isActive:"",
				latVal:"",
				lngVal:""
			}
		},
		methods: {
			zoomMap: function() { 
				this.mymap.setView([28.60287,77.32948], 17);
			},
			show: function(){
				const $this=this;
				this.isActive="is-active";
				
				this.mymap.addEventListener('click', function(e){
					$this.latVal =  e.latlng.lat.toFixed(5);
					$this.lngVal =  e.latlng.lng.toFixed(5);
				});
				// this. = this.mymap.click.latlng.lng.toFixed(5);

			},
			customEventFun: function() {
				this.isActive="";
			},

		},
		mounted() {
			const $this=this;
    		this.mymap = L.map(this.$refs['mapElement']).setView([20.5937, 78.9629],3);
    		L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(this.mymap);

	// L.marker([28.60287,77.32948]).addTo(this.mymap)
	//     .bindPopup('New Delhi')
	//     .openPopup();
		this.geojsonlayer = new L.GeoJSON.AJAX('geodb/', {

					pointToLayer: function(feature, latlng) {
					const name = feature.properties.name;
					const idAttrName = name.replace(/ /g,'');
					const str = `
					<button id="zoomTo${idAttrName}" class="button is-primary"> 
					<span>${name}</span>
    				<span class="icon is-small" id="close${idAttrName}">
     					<i class="fa fa-times-circle"></i>
     				</span>
					</button>
					`;

					$this.root.mapLocationListEl += str;


					const newStr =`<h4>${name}</h4><hr>
					<a href='${feature.properties.web}' target="blank">
					<img src='/static/img/${feature.properties.image}' width='200px'/>
					</a>`;

					$this.$nextTick(function () {
						document.getElementById(`zoomTo${idAttrName}`).addEventListener("click", function(){
							$this.mymap.setView([latlng.lat, latlng.lng],17)		  
						});

						document.getElementById(`close${idAttrName}`).addEventListener("click", function(e){
								e.target.parentNode.parentNode.remove();
						});

					});
				
					return L.marker(latlng).bindPopup(newStr);

				}
		});

		this.geojsonlayer.addTo(this.mymap);
        // this.mymap.fitBounds(this.geojsonlayer.getBounds());

		// $this.$nextTick(function() { 
		// 	document.getElementById("btnBuffer").addEventListener("click", function(){
		// 		if (document.getElementById('btnBuffer').innerText == 'Buffer'){
		// 			const bufferAttractions = turf.buffer($this.geojsonlayer.toGeoJSON(), 1, {units: 'miles'});
		// 			this.bufferLayer = L.geoJSON(bufferAttractions).addTo($this.mymap);
		// 			document.getElementById('btnBuffer').innerText = "Remove Buffer";
		// 		} else {
		// 			$this.mymap.removeLayer(this.bufferLayer);
		// 			document.getElementById('btnBuffer').innerText = "Buffer";
		// 		}
		// 	});
		// });
		// this.mymap.addEventListener('mousemove',e => {
		// 	const str = "Latitude: "+ e.latlng.lat.toFixed(5)+ " Longitude: "+ e.latlng.lng.toFixed(5)+ " Zoom Level: "+ this.mymap.getZoom();
		// 	document.getElementById('map_coords').innerHTML = str;

		// });



		
    
  	},
  	components : {
  		mapmodal:mapmodal
  	},
  	created: function() {
		this.mapmodal = this.$children;
		this.root = this.$parent;
	}
};
</script>