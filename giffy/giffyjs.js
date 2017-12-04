// JavaScript File
/*global location $*/
var searchTerm;
$("#submit").click(function() {
    console.log("hello");
    searchTerm= $("#input").val();
    // http://api.openweathermap.org/data/2.5/weather?q=newyork&units=imperial&appid=e8b0f6b65e53e6aac625bad6fdc0e91f
    $.getJSON(
        "https://api.giphy.com/v1/gifs/search?q=" + searchTerm + "&api_key=dc6zaTOxFJmzC",
        
        function(response) {
            console.log(response);
            $("#gif").html("<img src=" + response.data[Math.floor(Math.random()*response.data.length)].images.fixed_width_downsampled.url + ">");
        }
    );
    
        
});

$("#reset").click(function() { 
    location.reload();
    
});
