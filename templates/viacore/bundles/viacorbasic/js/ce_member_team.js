
$(document).ready(function() {
    var textContainerWidth = $('.ce_memberteam .innerbox .text_content').width();
    $('.team-member-slider .slider-control .swiper-scrollbar').width(textContainerWidth);
    $(window).resize(function() {
        var textContainerWidth = $('.ce_memberteam .innerbox .text_content').width();
        $('.team-member-slider .slider-control .swiper-scrollbar').width(textContainerWidth);
    });
    var arrowPrev = $('.team-member-slider .slider-control .slider-prev');
    var arrowNext = $('.team-member-slider .slider-control .slider-next');
    var sliderInnerBoxMarginLeft = $('.ce_memberteam .innerbox').css('margin-left');
    var sliderInnerBoxMarginRight = $('.ce_memberteam .innerbox').css('margin-right');
    if ($(window).width() > 1024) {
        arrowPrev.css({
            'left': sliderInnerBoxMarginLeft
        });
        arrowNext.css({
            'right': sliderInnerBoxMarginRight
        });
    } else {
        arrowPrev.css({
            'left': '7%'
        });
        arrowNext.css({
            'right': '7%'
        });
    }
    $(window).resize(function() {
        var arrowPrev = $('.team-member-slider .slider-control .slider-prev');
        var arrowNext = $('.team-member-slider .slider-control .slider-next');
        var sliderInnerBoxMarginLeft = $('.ce_memberteam .innerbox').css('margin-left');
        var sliderInnerBoxMarginRight = $('.ce_memberteam .innerbox').css('margin-right');
        if ($(window).width() > 1024) {
            arrowPrev.css({
                'left': sliderInnerBoxMarginLeft
            });
            arrowNext.css({
                'right': sliderInnerBoxMarginRight
            });
        } else {
            arrowPrev.css({
                'left': '7%'
            });
            arrowNext.css({
                'right': '7%'
            });
        }
    });
});