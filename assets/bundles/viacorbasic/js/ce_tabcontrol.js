
$(document).ready(function() {
    $('.nav-item .nav-link').click(function(e) {
        e.preventDefault();
        var tab_id = $(this).attr('data-tab');
        $('.ce_tabcontrol .nav-item .nav-link').removeClass('active');
        $('.tab-content .tab-pane').removeClass('active');
        $(this).addClass('active');
        $(".tab-content #" + tab_id).addClass('active');
    });
});