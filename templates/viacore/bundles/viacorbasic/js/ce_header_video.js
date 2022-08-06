
$(window).on('load', function() {
    if ($(window).width() <= 1024) {
        $('.header-video-wrapper video source').attr('src', 'files/videos/hp-video-s-loop.mp4');
        //console.log('small screen loop on load');
    } else {
        $('.header-video-wrapper video source').attr('src', 'files/videos/hp-video-l-loop.mp4');
        //console.log('large screen loop on load');
    }
});
$(document).ready(function() {
    $('.header-video-play').click(function() {
        var headerVideo = $(this).parent().prev().find('video').get(0);
        var headerVideoSrc = $(this).parent().prev().find('video source');
        $(this).parent().prev().removeClass('overlayed');
        if ($(this).parent().hasClass('video-playing')) {
            headerVideo.paused ? headerVideo.play() : headerVideo.pause();
            $(this).parent().toggleClass('video-paused');
        } else {
            $(headerVideo).removeAttr(' loop autoplay');
            if ($(window).width() <= 1024) {
                headerVideoSrc.attr('src', 'files/videos/hp-video-s-full.mp4');
                //console.log('smaller screen');
            } else {
                headerVideoSrc.attr('src', 'files/videos/hp-video-l-full.mp4');
                //console.log('big screen');
            }
            headerVideo.muted = false;
            headerVideo.load();
            headerVideo.play();
            $(this).parent().addClass('video-playing');
            $(this).parent().parent().addClass('video-playing'); //Remove if doesnt help for styling
        }
    });
    var headerVid = $('.header-video-wrapper video').get(0);
    $(headerVid).on('ended', function() {
        $(this).parent().addClass('overlayed');
        $(this).parent().next().removeClass('video-playing');
        $(this).parent().parent().removeClass('video-playing'); //Remove if doesnt help for styling
        if ($(window).width() < 1024) {
            $(headerVid).find('source').attr('src', 'files/videos/hp-video-s-loop.mp4');
        } else {
            $(headerVid).find('source').attr('src', 'files/videos/hp-video-l-loop.mp4');
        }
        headerVid.muted = true;
        headerVid.load();
        headerVid.play();
    });
});