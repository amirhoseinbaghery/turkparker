
$(document).ready(function() {
    var loadedFilter = window.location.hash.replace("#", "");
    var systemTeaser = $('.system-list-grid .system-teaser');
    var subCatCard = $('.card-slider .ce_subcategorycard');
    var systemSideFilter = $('.system-filters-wrap .system-teaser-filter:not([data-subcategory="*"])');
    var systemSideAll = $('.system-filters-wrap .system-teaser-filter[data-subcategory="*"]');
    if (window.location.hash == '') {
        systemTeaser.removeClass('system-teaser-hidden');
        systemSideAll.addClass('filter-active');
    } else {
        subCatCard.filter((i, el) => $(el).data('subcategory').includes(loadedFilter)).addClass('card-active');
        systemSideFilter.filter((i, el) => $(el).data('subcategory').includes(loadedFilter)).addClass('filter-active');
        systemTeaser.addClass('system-teaser-hidden');
        systemTeaser.filter((i, el) => $(el).data('subcategory').includes(loadedFilter)).removeClass('system-teaser-hidden');
    }
    $(systemSideFilter).click(function(e) {
        var clickedFilter = $(this).data('subcategory');
        window.location.hash = clickedFilter;
        e.preventDefault();
    });
    $(subCatCard).click(function() {
        var clickedSubCatCard = $(this).data('subcategory');
        if ($(this).hasClass('card-active')) {
            $(this).removeClass('card-active');
            systemSideFilter.removeClass('filter-active');
            systemSideAll.addClass('filter-active');
            systemTeaser.removeClass('system-teaser-hidden');
            history.pushState("", document.title, window.location.pathname);
        } else {
            systemSideFilter.filter((i, el) => $(el).data('subcategory').includes(loadedFilter)).addClass('filter-active');
            window.location.hash = clickedSubCatCard;
        }
    });
    $(window).on('hashchange', function(e) {
        var changedHash = window.location.hash.replace("#", "");
        systemSideAll.removeClass('filter-active');
        systemSideFilter.removeClass('filter-active');
        systemSideFilter.filter((i, el) => $(el).data('subcategory').includes(changedHash)).addClass('filter-active');
        subCatCard.removeClass('card-active');
        subCatCard.filter((i, el) => $(el).data('subcategory').includes(changedHash)).addClass('card-active');
        systemTeaser.addClass('system-teaser-hidden').css('animationName', '');
        systemTeaser.filter((i, el) => $(el).data('subcategory').includes(changedHash)).removeClass('system-teaser-hidden').css('animationName', 'systemTeaserReScale');
    });
    $(systemSideAll).click(function(e) {
        history.pushState("", document.title, window.location.pathname);
        systemTeaser.removeClass('system-teaser-hidden');
        subCatCard.removeClass('card-active');
        systemSideFilter.removeClass('filter-active');
        $(this).addClass('filter-active');
        e.preventDefault();
    });
});
//ce_subcategorycard.js & productfilter.js should be obsolete now - check before deleting or make a local back up and test