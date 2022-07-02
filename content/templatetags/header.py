from django import template

from content.models import SiteSetting, About, Communication, SocialMedia

register = template.Library()


@register.inclusion_tag('partial/menu.html')
def menu(request):
    app = request.resolver_match.app_names[0]
    app_ = request.resolver_match.url_name
    about_ = About.objects.all().first()
    communicate = Communication.objects.all().first()
    return {
        'object': about_,
        'com': communicate,
        'app': app,
        'app_': app_,
    }


@register.inclusion_tag('partial/logo.html')
def logo():
    return {
        'logo': SiteSetting.objects.last(),
    }


@register.inclusion_tag('partial/social.html')
def social():
    return {
        'social': SocialMedia.objects.all(),
    }


@register.inclusion_tag('partial/com.html')
def com():
    return {
        'com': Communication.objects.last(),
    }
