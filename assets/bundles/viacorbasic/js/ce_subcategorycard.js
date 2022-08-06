
//This file is obsolete, since all the functions are happening in systemfilter.js
/*$(document).ready(function() {
    $('.card-slider .ce_subcategorycard').click(function() {
        var clickedSubCatCard = $(this).data('subcategory');
        if($(this).hasClass('card-active')) {
            $(this).removeClass('card-active');
            //$('.system-list-grid .system-teaser').removeClass('system-teaser-hidden');
            //$('.system-filters-wrap .system-teaser-filter[data-subcategory="*"]').addClass('filter-active');
            history.pushState("", document.title, window.location.pathname);
        } else {
            $('.card-slider .ce_subcategorycard').removeClass('card-active');
            $(this).addClass('card-active');
            //$('.system-filters-wrap .system-teaser-filter').filter((i, el) => $(el).data('subcategory').includes(loadedFilter)).addClass('filter-active');
            //$('.system-list-grid .system-teaser').addClass('system-teaser-hidden');
            //$('.system-list-grid .system-teaser').filter((i, el) => $(el).data('subcategory').includes(loadedFilter)).removeClass('system-teaser-hidden');
            window.location.hash = clickedSubCatCard;
        }
    });
});*/