from django import template

from product.models import Product, ProductCategory

register = template.Library()


@register.inclusion_tag('partial/ProductCategory.html')
def ProductCategoryTT():
    return {
        'category': ProductCategory.objects.filter(status='p'),
        'recently': Product.objects.filter(status='p')[:3],
    }
