from django.urls import path

from project.models import Project, ProjectCategory, ProjectTag, ProjectComment

app_name = 'project'
urlpatterns = [
    # path('<slug>', Project, name='project'),
    # path('', ProjectCategory.as_view(), name='project_home'),
    # path('category/<slug>', ProjectTag.as_view(), name='project_category'),
    # path('tag/<slug>', ProjectComment.as_view(), name='project_tag'),
]
