from django.urls import path

from blog.views import SinglePost, PostList, categoryList, tagList, Author, SearchBlog

app_name = 'blog'
urlpatterns = [
    path("search/", SearchBlog.as_view(), name="search"),
    path('<slug>', SinglePost, name='SinglePost'),
    path('', PostList.as_view(), name='PostList'),
    path('category/<slug>', categoryList.as_view(), name='categoryList'),
    path('tag/<slug>', tagList.as_view(), name='tagList'),
    path('author/<slug:username>', Author.as_view(), name='Author'),
]
