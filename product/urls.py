from django.urls import path

from product.views import product, ProductList, ProductCategoryList, ProductTagList, SearchProduct

app_name = 'product'
urlpatterns = [
    path('category/<slug>', ProductCategoryList.as_view(), name='categoryList'),

    path("search/", SearchProduct.as_view(), name="search"),
    path('<slug>', product, name='product'),
    path('', ProductList.as_view(), name='ProductList'),
    path('tag/<slug>', ProductTagList.as_view(), name='tagList'),
]
