/*
	network.js
	XE401/XE402 - NetGrok II
	Tyler Reece, Dan Young, Matt Kim, Josh Balba
	United States Military Academy
*/


/* VisJS setup */
var nodes = new vis.DataSet();
var edges = new vis.DataSet();

var container = document.getElementById('visualization');
var data = {
	nodes: nodes,
	edges: edges
};

var options = {
	nodes: {
		brokenImage: "https://i.dlpng.com/static/png/6818_preview.png",
		font: {
			multi: 'html',
		},
	},
	interaction: {
		hover: true,
	},
	physics: {
		enabled: true,
		stabilization: false,
		barnesHut: {
			gravitationalConstant: -2000,
			centralGravity: 0.3,
			avoidOverlap: 0.5,
			
		},		
	},
	layout: {
		randomSeed: 2,
	},
};

var network = new vis.Network(container, data, options);


/* Add initial informational node on empty network */
if(!nodes.length) {
	nodes.add({id: 0, label: "<b>Browse around to start Grokking!</b>"});
};

	
/* Connect to socket */
var socket = io.connect('http://' + document.domain + ':' + location.port);

/* On connect message to console */
socket.on('connect', function() {
	console.log("Client connected successfully!");
	console.log(navigator.userAgent);
	socket.emit('send whole graph', {userAgent: navigator.userAgent});
});

socket.on('whole graph', function (msg) {
	console.log(msg);
});

/* Handle creation of new node */
socket.on('new node', function(msg) { 	
	console.log(msg);	
	/* Remove intro message on browsing start */
	if(nodes.get(0)){
		nodes.remove(0)
	};
	
	var json_obj = JSON.parse(msg);
       	var host = json_obj.host;
	
	nodes.add({label: '<b>' + host + '</b>', image: 'https://' + host + '/favicon.ico', shape: 'image'});
	network.fit();
});

/* Print information to console for debuging */
socket.on('debug', function(msg) {
       	console.log(msg);
});

