window.onscroll = function () {
    if (window.pageYOffset > 5) {
        document.getElementById('for-b').style.top = 0;
        document.querySelector('.logo-fixed').style.display = "block";
    } else {
        document.getElementById('for-b').style.top = 50 + 'px';
        document.querySelector('.logo-fixed').style.display = "none";
    }
};
window.onload = function () {
    if (document.getElementById('burger').checked == true) {
        document.getElementById('#span-one').style.rotate = 584 + "deg";
    }
}
$('.sl').slick({
    autoplay: true,
    autoplaySpeed: 3000,
    speed: 1000,
    cssEase: 'ease-in',
    centerPadding: '25px',
    dots: true,
    arrows: false,
    adaptiveHeight: true
});
