
$(document).ready(function() {
    //var swiper = new Swiper(".team-member-slider .content-slider");
    var teamSlider = new Swiper(".team-member-slider .content-slider", {
        direction: "horizontal",
        slidesPerView: 1,
        spaceBetween: 0,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev"
        },
        scrollbar: {
            el: ".swiper-scrollbar",
            draggable: true
        }
    });
    $('.team-members-filter-list .team-member-filter[data-team="*"]').parent().hide();
    $('.team-member-filter-button').click(function(e) {
        $(this).find('.team-filter-toggle').toggleClass('dropdown-expanded');
        $(this).next().slideToggle();
        e.preventDefault();
    });
    $('.team-members-filter-list .team-member-filter').click(function() {
        var teamMemberFilterText = $(this).text();
        var selectedFilter = $(this).data('team');
        $(this).parentsUntil('.team-members-filter-row').find('.team-member-filter-selected').text(teamMemberFilterText);
        $(this).parentsUntil('.team-members-filter-row').find('.team-filter-toggle').removeClass('dropdown-expanded');
        $(this).parent().parent().slideToggle();
        $('.team-members-filter-list .team-member-filter[data-team="*"]').parent().show();
        $('.swiper-slide.ce_memberteam').hide();
        $('.swiper-slide.ce_memberteam').filter((i, el) => $(el).data('team').includes(selectedFilter)).show();
        teamSlider.update();
        setTimeout(function() {
            teamSlider.scrollbar.updateSize();
        }, 500);
        return false;
    });
    $('.team-members-filter-list .team-member-filter[data-team="*"]').click(function() {
        $(this).parent().hide();
        $('.swiper-slide.ce_memberteam').show();
        teamSlider.update();
        setTimeout(function() {
            teamSlider.scrollbar.updateSize();
        }, 500);
    });
});