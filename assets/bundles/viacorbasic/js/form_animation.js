
$(document).ready(function() {
    $('.header_form form .widget input, .header_form form .widget textarea, .header_form form .widget select').each(function() {
        if (!$(this).val()) {
            $(this).prev().removeClass("labelUP");
        } else {
            $(this).prev().addClass("labelUP");
        }
        $(this).on('focusin', function() {
            $(this).prev().addClass("labelUP");
        });
        $(this).focusout(function() {
            if (!$(this).val()) {
                $(this).prev().removeClass("labelUP");
            } else {
                $(this).prev().addClass("labelUP");
            }
        });
    });
});