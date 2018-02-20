// Make socket connection
var socket = io.connect('http://127.0.0.1:8081');

socket.emit("chat", "hello");

socket.on('connect', function(){console.log(socket.id);});

socket.on('disconnect', function(){console.log("disconnect");});

socket.on('changed', function(data){
	// code for fetching the current leaderboard value
	console.log(data);
	content.innerHTML = data.data;
});



var btn = document.getElementById('send');
var content = document.querySelector('.content');

btn.addEventListener('click', function() {
	console.log("clicked");
	// emit the submit event when a question is submitted and is correct so the score is changed 
	// this is to let every one know that the score has been changed and they need to update the score
	socket.emit('submit', 'submitted');
});
