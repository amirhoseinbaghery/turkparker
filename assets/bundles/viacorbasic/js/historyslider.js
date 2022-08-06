
$(document).ready(function() {
    var historySlider = new Swiper(".historysection-slider", {
        direction: "vertical",
        slidesPerView: 1,
        mousewheel: true,
        scrollbar: {
            el: ".history-slider-scrollbar",
            draggable: true,
            //hide: true,
        }
    });
});