from django import template

from content.models import SiteSetting, SocialMedia, Communication
from product.models import Product, ProductCategory

register = template.Library()


@register.inclusion_tag('partial/ProductCategory.html')
def ProductCategoryTT():
    return {
        'category': ProductCategory.objects.filter(status='p'),
        'recently': Product.objects.filter(status='p')[:3],
    }


@register.inclusion_tag('partial/prodcontact.html')
def contact():
    return {
        'logo': SiteSetting.objects.last(),
        'social': SocialMedia.objects.all(),
        'com': Communication.objects.last(),
    }
