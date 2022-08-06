from django import template

from blog.models import BlogCategory
from content.models import SiteSetting, About, Communication, SocialMedia
from product.models import ProductCategory

register = template.Library()


@register.inclusion_tag('partial/menu.html')
def menuProduct():
    category = ProductCategory.objects.filter(status='p', subClass=None)
    return {
        'object': category,
    }


@register.inclusion_tag('partial/menuBlog.html')
def menuBlog():
    category = BlogCategory.objects.filter(status='p', subClass=None)
    return {
        'object': category,
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
