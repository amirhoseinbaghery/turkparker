from django.urls import path

from product.views import product
from project.models import Project, ProjectCategory, ProjectTag, ProjectComment

app_name = 'product'
urlpatterns = [
    path('<slug>', product, name='product'),
    # path('', ProjectCategory.as_view(), name='project_home'),
    # path('category/<slug>', ProjectTag.as_view(), name='project_category'),
    # path('tag/<slug>', ProjectComment.as_view(), name='project_tag'),
]
