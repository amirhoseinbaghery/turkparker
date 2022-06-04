from django.urls import path

from blog.views import SinglePost, PostList, categoryList, tagList, Author

app_name = 'blog'
urlpatterns = [
    path('<slug>', SinglePost, name='SinglePost'),
    path('', PostList.as_view(), name='PostList'),
    path('category/<slug>', categoryList.as_view(), name='categoryList'),
    path('tag/<slug>', tagList.as_view(), name='tagList'),
    path('author/<slug:username>', Author.as_view(), name='Author'),
]
