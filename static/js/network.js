String.prototype.hashCode = function() {
	var hash = 0, i, chr;
	if (this.length === 0) return hash;
	for (i = 0; i < this.length; i++) {
		chr   = this.charCodeAt(i);
		hash  = ((hash << 5) - hash) + chr;
		hash |= 0; // Convert to 32bit integer
	}
	return hash;
};

function getCoordinates(host) {
	var a = host.hashCode();
	var b = Math.abs(a) % 1000000;
	var x = (b / 100000) * 100;
	var y = (((b / 10000) >> 0)% 10)*100;
	var x1 = ((b % 10000) / 1000) * 10;
	var y1 = ((b % 1000) / 100)*10;
	var x2 = (b % 100) / 10;
	var y2 = (b % 10);
	x = Math.floor(x + x1 + x2);
	y = Math.floor(y + y1 + y2);
	return [x,y];
}

var nodesSeen = new Set();

/* VisJS setup */
var nodes = new vis.DataSet([]);
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
        stabilization: true,
        barnesHut: {
            gravitationalConstant: -1000,
            centralGravity: 0,
            avoidOverlap: 0.25,

        },
    },
    layout: {
        randomSeed: 2,
    },
};

var network = new vis.Network(container, data, options);

network.moveTo({
	position: {x: 500, y:500},
	offset: {x: 500, y:  500},
});

/* Network Functions */
function addNode(json_string) {
    var json_obj = JSON.parse(json_string);
	if(!nodesSeen.has(json_obj.host)) {
    	nodesSeen.add(json_obj.host);
		var x = getCoordinates(json_obj.host)[0];
		var y = getCoordinates(json_obj.host)[1];
		nodes.add({
        	label: '<b>' + json_obj.host + '</b>',
			src_ip: json_obj.src_ip,
			src_port: json_obj.src_port,
			dst_ip: json_obj.dst_ip,
			dst_port: json_obj.dst_port,
			time_start: json_obj.time_start,
			time_end: json_obj.time_end,
			download: json_obj.download,
			upload: json_obj.upload,
			protocol: json_obj.protocol,
        	image: 'https://' + json_obj.host + '/favicon.ico',
        	shape: 'image',
			x: x,
			y: y,
    	});
	}
    network.fit();
}

function addNodes(json_strings) {
    var j_strings = json_strings.split('}');
    //console.log(j_strings);
    for (var i = 0; i < j_strings.length - 1; i++) {
        var newString = (j_strings[i] + '}').split("'").join('"');
        addNode(newString);
    }

}

/* Connect to socket */
var socket = io.connect('http://' + document.domain + ':' + location.port);

/* On connect message to console */
socket.on('connect', function() {
    socket.emit('send whole graph', {
        userAgent: navigator.userAgent
    });
});

/* On receipt of current state */
socket.on('whole graph', function(msg) {
	addNodes(msg);
});

/* Handle creation of new node */
socket.on('new node', function(msg) {
    addNode(msg);
});

/* Print information to console for debuging */
socket.on('debug', function(msg) {
    console.log(msg);
});

/* User Events */

network.on('hoverNode', function(properties) {
	var hoveredNodes = nodes.get(properties.node);
	var table = "<table>" +
			"<tr>" +
				"<th>Host</th>" +
				"<th>Protocol</th>" +
				"<th>Source IP</th>" +
				"<th>Source Port</th>" +
				"<th>Destination IP</th>" +
				"<th>Destination Port</th>" +
				"<th>Time Start</th>" +
				"<th>Time End</th>" +
				"<th>Download</th>" +
				"<th>Upload</th>" +
			"</tr>" + 
			"<tr>" +
				"<td>" + hoveredNodes.label + "</td>" +
				"<td>" + hoveredNodes.protocol + "</td>" +
			   	"<td>" + hoveredNodes.src_ip + "</td>" +
				"<td>" + hoveredNodes.src_port + "</td>" +
				"<td>" + hoveredNodes.dst_ip + "</td>" +
				"<td>" + hoveredNodes.dst_port + "</td>" +	
				"<td>" + hoveredNodes.time_start + "</td>" +
				"<td>" + hoveredNodes.time_end + "</td>" +
				"<td>" + hoveredNodes.download + "</td>" +
				"<td>" + hoveredNodes.upload + "</td>" +
			"</tr>" +
			"</table>"

	var info = document.getElementById('info').innerHTML = table;
});

network.on('blurNode', function(properties) {
	var hoveredNodes = nodes.get(properties.node);
	document.getElementById('info').innerHTML = '';
});
