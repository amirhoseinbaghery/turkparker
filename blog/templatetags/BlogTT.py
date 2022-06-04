from django import template

from blog.models import BlogCategory, Blog, BlogTag

register = template.Library()


@register.inclusion_tag('partial/category.html')
def PostCategory():
    return {
        'category': BlogCategory.objects.filter(status='p'),
        'recently': Blog.objects.filter(status='p')[:3],
    }
