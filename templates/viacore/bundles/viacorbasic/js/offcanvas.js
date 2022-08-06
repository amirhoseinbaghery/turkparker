
$(document).ready(function() {
    //Open function
    $('.offcanvas-open').click(function() {
        $('#offcanvas').addClass('canvas-open');
        var scrollY = document.documentElement.style.getPropertyValue('--scroll-y');
        document.body.style.position = 'fixed';
        document.body.style.overflowY = 'scroll';
        document.body.style.top = `-${scrollY}`;
        return false;
    });
    //Close function
    $('.offcanvas-close').click(function() {
        $(this).parentsUntil('body').removeClass('canvas-open');
        const scrollY = document.body.style.top;
        document.body.style.position = '';
        document.body.style.top = '';
        window.scrollTo(0, parseInt(scrollY || '0') * -1);
        document.body.style.overflowY = 'auto';
        return false;
    });
});
//Track page scroll
window.addEventListener('scroll', () => {
    document.documentElement.style.setProperty('--scroll-y', `${window.scrollY}px`);
});
//Screen Height Fix for Safari OS - Phones 
//See CSS also
const screenHeight = () => {
    const doc = document.documentElement;
    doc.style.setProperty('--screen-height', `${window.innerHeight}px`);
}
window.addEventListener('resize', screenHeight);
screenHeight();