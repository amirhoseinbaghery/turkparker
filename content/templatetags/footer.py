from django import template
from content.models import SiteSetting, About, Communication, Licence

register = template.Library()


@register.inclusion_tag('partial/footer.html')
def footer():
    about_ = About.objects.all().last()
    communicate = Communication.objects.all().last()
    return {
        'object': about_,
        'com': communicate,
        'logo': SiteSetting.objects.last(),
        'licence': Licence.objects.all()
    }
