from django import template

from project.models import Project, ProjectCategory

register = template.Library()


@register.inclusion_tag('partial/ProjectCategory.html')
def ProjectCategoryTT():
    return {
        'category': ProjectCategory.objects.all(),
        'recently': Project.objects.filter(status='p')[:3],
    }
