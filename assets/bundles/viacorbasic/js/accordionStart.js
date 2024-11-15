
jQuery(function($) {
    $(document).accordion({
        // Put custom options here
        heightStyle: 'content',
        header: '.toggler',
        collapsible: true,
        create: function(event, ui) {
            ui.header.addClass('active');
            $('.toggler').attr('tabindex', 0);
        },
        activate: function(event, ui) {
            ui.newHeader.addClass('active');
            ui.oldHeader.removeClass('active');
            $('.toggler').attr('tabindex', 0);
        }
    });
});