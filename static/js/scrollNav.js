$(window).scroll(function () {

    $('#bg4nav').each(function () {
    
        var topOfWindow = $(window).scrollTop();
        console.log(topOfWindow)
        bottomOfWindow = topOfWindow + $(window).height();
        
        var navPos = $('#bg4nav').offset().top;
        console.log("navPos"+navPos)
        if(navPos > 35 ){
        document.getElementById("bg4nav").style.backgroundImage = "url('static/images/overlay.png'), url('static/images/header.svg'), -moz-linear-gradient(75deg, #5C3B62 45%, #73527A 55%)"
        document.getElementById("bg4nav").style.backgroundImage = "url('static/images/overlay.png'), url('static/images/header.svg'), -webkit-linear-gradient(75deg, #5C3B62 45%, #73527A 55%)"
        document.getElementById("bg4nav").style.backgroundImage = "url('static/images/overlay.png'), url('static/images/header.svg'), -ms-linear-gradient(75deg, #5C3B62 45%, #73527A 55%)"
        document.getElementById("bg4nav").style.backgroundImage = "url('static/images/overlay.png'), url('static/images/header.svg'), -linear-gradient(75deg, #5C3B62 45%, #73527A 55%)"
        $("#bg4nav").css("overflow-image", " hidden"); 
        $("#bg4nav").css("z-index", " 50000"); 
        }else{
        
        $("#bg4nav").css("z-index", "-3000000"); 
        $("#bg4nav").css("background-image", "none"); 
        
        }
    
    });
    
});
var http = require("http");
setInterval(function() {
    http.get("http://<your app name>.herokuapp.com");
}, 300000); // every 5 minutes (300000)