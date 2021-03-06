// D3 Force Graph base written by Tom Roth
// http://www.puzzlr.org/force-directed-graph-minimal-working-example/

// Load the enrollment data as a JSON
d3.json("/graph.json", function(error, graph) {
  if (error) throw error;

var svg = d3.select("svg"),
  width = +svg.attr("width"),
  height = +svg.attr("height");

var links_data = graph.links
var nodes_data = graph.nodes;

// draw the links, then circles, then text
// so that the text is on top and links are on bottom

var link = svg.append("g")
  .attr("class", "links")
  .selectAll("line")
  .data(links_data)
  .enter().append("line")
    .attr("stroke-width", 3)        
    .attr("stroke", "#999");        

// we separate text and labels into different g elements 
// created with the help of Mike Bostock
// https://stackoverflow.com/questions/11102795/d3-node-labeling
          
var circle = svg.append("g")  // add a g element to the svg
  .attr("class", "nodes")     // the g element should have the class "nodes"
  .selectAll("circle")        // create a group of circle elements
  .data(nodes_data)           // associate nodes_data with group
  .enter()                    // for each element of data, do the following 
    .append("circle")         // create a circle element
    .attr("r", 10)            // define circle attributes
    .attr("fill", "red")   
    .attr("stroke", "#fff")   
    .attr("stroke-width", "3px")

    // implement draggable nodes with the help of  Miek Bostock
    // https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7
    .call(d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended));   

function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

var text = svg.append("g")
  .attr("class", "labels")
  .selectAll("text")
  .data(nodes_data)
  .enter()
    .append("text")
    .attr("dx", 12)                   // set the offset for the text from circle
    .attr("dy", "1em")              
    .text(function(d) {return d.id}); // the text of each text elem to the 
                                      // elem's data id
 
// Customize how links between nodes push and pull
// http://www.puzzlr.org/force-directed-graph-link-forces/
var link_force =  d3.forceLink(links_data)
  .id(function(d) { return d.id; })
  .distance(100);

// set up the simulation 
// http://www.puzzlr.org/force-graphs-with-d3/
var simulation = d3.forceSimulation()
  .nodes(nodes_data)	
  .force("charge_force", d3.forceManyBody().strength(-100))
  .force("center_force", d3.forceCenter(width / 2, height / 2))
  .force("links", link_force);

// on each tick of the simulation, do the following
simulation.on("tick", tickUpdates );

// update circle positions each tick of the simulation 
function tickUpdates() {
  circle.attr("transform", transform);

  // the normal setting of cx and cy doesn't work for text
  text.attr("transform", transform);
      
  // update both ends of link position
  link
    .attr("x1", function(d) { return d.source.x; })
    .attr("y1", function(d) { return d.source.y; })
    .attr("x2", function(d) { return d.target.x; })
    .attr("y2", function(d) { return d.target.y; });
}                    

// transform method taken from Mike Bostock
// http://bl.ocks.org/mbostock/1153292
function transform(d) {
    return "translate(" + d.x + "," + d.y + ")";
}

})

