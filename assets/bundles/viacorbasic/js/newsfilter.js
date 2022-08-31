
$(document).ready(function() {
    var loadedFilter = window.location.hash.replace("#", "");
    if (window.location.hash == '') {
        $('.news_teaser').removeClass('news_teaser-hidden');
        $('.news_teaser-filter[data-filter="*"]').addClass('filter-active');
        $('.additional-filters-container').addClass('no-filter-selected');
    } else {
        $('.news_teaser').addClass('news_teaser-hidden');
        $('.news_teaser').filter((i, el) => $(el).data('filter').includes(loadedFilter)).removeClass('news_teaser-hidden');
        $('.news_teaser-filter').filter((i, el) => $(el).data('filter').includes(loadedFilter)).addClass('filter-active');
        $('.news_teaser-filter-button').addClass('active');
    }
    $('.news_teaser-filter').click(function(e) {
        var clickedFilter = $(this).attr('data-filter');
        $('.news_teaser').addClass('news_teaser-hidden').css('animationName', '');
        $('.news_teaser').filter((i, el) => $(el).data('filter').includes(clickedFilter)).removeClass('news_teaser-hidden').css('animationName', 'newsTeaserReScale');
        $('.news_teaser-filter').removeClass('filter-active');
        $(this).addClass('filter-active');
        $('.select-filter-button').filter((i, el) => $(el).data('filter') == clickedFilter).addClass('filter-active2');
        $('.additional-filters-container').removeClass('no-filter-selected');
        e.preventDefault();
    });
    $('.news_teaser-filter:not([data-filter="*"])').click(function() {
        var activeFilter = $(this).attr('data-filter');
        window.location.hash = activeFilter;
    });
    $('a.news_teaser-filter[data-filter="*"]').click(function() {
        $('.news_teaser').removeClass('news_teaser-hidden');
        $('.additional-filters-container').addClass('no-filter-selected');
        history.pushState("", document.title, window.location.pathname);
    });
    $('.news_teaser-filter-button').click(function() {
        $('.additional-filters-container').appendTo('#offcanvas .offcanvas-content').show();
        return false;
    });
    $('.additional-filters-container .select-filter-button').click(function() {
        var clickedFilterBtn = $(this).attr('data-filter');
        $('.news_teaser-filter-button').addClass('active');
        $(".news_teaser-filter").filter((i, el) => $(el).data('filter') == clickedFilterBtn).addClass('filter-active');
    });
    $('.news_teaser-filters-wrap .news_teaser-filter').click(function() {
        $('.news_teaser-filter-button').removeClass('active');
    });
    $('.additional-filters-container .clear-filter-button').click(function() {
        $('.news_teaser-filter-button').removeClass('active');
        $('.additional-filters-container').addClass('no-filter-selected');
        $('a.news_teaser-filter[data-filter="*"]').addClass('filter-active');
    });
});
//Convert Filter List into Toggle on 414px screen and below
$(document).ready(function() {
    if ($(window).width() <= 414) {
        $('.offcanvas-filter-list').each(function() {
            $(this).hide();
            $(this).prev().addClass('filter-toggle-title');
        });
    }
    $('.filter-toggle-title').each(function() {
        $(this).click(function() {
            $(this).toggleClass('filter-toggle_expanded');
            $(this).next('.offcanvas-filter-list').slideToggle();
        });
    });
});
$(window).resize(function() {
    if ($(window).width() <= 414) {
        $('.offcanvas-filter-list').each(function() {
            $(this).hide();
            $(this).prev().addClass('filter-toggle-title');
        });
    } else {
        $('.offcanvas-filter-list').each(function() {
            $(this).show();
            $(this).prev().removeClass('filter-toggle-title');
        });
    }
});