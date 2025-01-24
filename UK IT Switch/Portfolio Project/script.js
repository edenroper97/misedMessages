window.onscroll = function() {
    var image = document.getElementById("eden-image");
    var welcome = document.getElementById("intro-text");
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    var windowHeight = window.innerHeight;

    //calculate opactiy based on scroll position

    var opacity = 1 - (scrollTop / windowHeight);
    if (opacity < 0){
        opacity = 0;
    }

    image.style.opacity = opacity;
    welcome.style.opacity = opacity;
}

