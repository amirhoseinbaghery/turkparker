
$(document).ready(function() {
    var cardSlider = new Swiper(".card-slider .content-slider", {
        direction: "horizontal",
        slidesPerView: "auto",
        //spaceBetween: 0,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev"
        },
        scrollbar: {
            el: ".swiper-scrollbar",
            draggable: true
        }
    });
});