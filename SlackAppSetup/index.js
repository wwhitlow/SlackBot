//Import the http module into JS
var http = require('http');

//Designate the PORT that is going to be opened up to the Web
const PORT=4390;

//Provide a Response for any type of Request coming to the server
function handleRequest(request, response) {
    response.end('Ngrok is working!  -  Path Hit: ' + request.url);
}

//Create the Server
var server = http.createServer(handleRequest);

//Start the Server listening on the designated port
server.listen(PORT, function() {
    console.log("Server listening on: http://localhost:%s", PORT);
});
