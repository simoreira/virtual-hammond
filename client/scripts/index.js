// Paralax effect in the header
var bg = document.querySelector('.header');
var c = 0;

setInterval(function() {
    bg.style.backgroundPosition = -c+"px 0px"; //move image to the left..remove the "-" if want to move right
    c++;
}, 60);

// Toggle navbar transparency depending where we are on the page
$(window).scroll(function () {
    var top = $(document).scrollTop();

    $('.jumbotron').css({
        'background-position': '0px -'+(top/3).toFixed(2)+'px'
    });

    if(top > 50)
    {
        $('.header > .navbar').removeClass('navbar-transparent');
    }
    else
    {
        $('.header > .navbar').addClass('navbar-transparent');
    }
});
