import Vue from "vue";
// import * as L from "leaflet" ;
import "./js/components/main.js";


new Vue({
	delimiters: ['[[', ']]'],
	el: '#mapAPP',
	data : {
		message:"testing message",
		mapLocationListEl:"",
	},
	methods: {
		removeButton: function(elementId) {
			document.getElementById(elementId).remove();
			// this.items.splice(index, 1);
		}
	},
	created: function() {
      
    },
});