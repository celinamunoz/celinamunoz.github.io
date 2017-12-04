// JavaScript File
/*global location $*/
var searchTerm;
$("#go").click(function() {
    console.log("hello");
    searchTerm= $("#input").val();
    //http://api.openweathermap.org/data/2.5/weather?q=newyork&units=imperial&appid=e8b0f6b65e53e6aac625bad6fdc0e91f
    $.getJSON(
        "http://api.openweathermap.org/data/2.5/weather?q=" + searchTerm + "&units=imperial&appid=e8b0f6b65e53e6aac625bad6fdc0e91f",
        
        function(response) {
            console.log(response);
            
            
              $("#weather-results").append("<div>" + "Temp: " + response.main.temp + "</div>" + "<div>" + "Pressure: " +response.main.pressure + "</div>" + "<div>" + "Humidity: " + response.main.humidity + "</div>" + "<div" + response.main.temp_min + "</div>");
          }
        )
});

$("#reset").click(function() { 
    location.reload();
    
});