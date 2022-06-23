from django.urls import path

from project.views import single_project, ProjectList, ProjectTagList, ProjectCategoryList, SearchProject

app_name = 'project'
urlpatterns = [
    path('category/<slug>', ProjectCategoryList.as_view(), name='CategoryList'),
    path("search/", SearchProject.as_view(), name="search"),
    path('<slug>', single_project, name='Project'),
    path('', ProjectList.as_view(), name='ProjectList'),
    path('tag/<slug>', ProjectTagList.as_view(), name='tagList'),
]
