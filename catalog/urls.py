from django.urls import path

from catalog.views import CatalogList

app_name = 'catalog'
urlpatterns = [
    path('', CatalogList.as_view(), name='List'),
]
