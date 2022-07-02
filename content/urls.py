from django.contrib.sitemaps.views import sitemap
from django.urls import path

from content.sitemap import BlogSitemap, ProjectSitemap, ProductSitemap, StaticViewSitemap, BCSitemap, BTSitemap, \
    PCSitemap, PTSitemap, ProductCSitemap, ProductTSitemap
from content.views import about, contactus, home

app_name = 'content'
sitemaps = {
    'blog': BlogSitemap,
    'project': ProjectSitemap,
    'product': ProductSitemap,
    'url': StaticViewSitemap,
    'BCSitemap': BCSitemap,
    'BTSitemap': BTSitemap,
    'PCSitemap': PCSitemap,
    'PTSitemap': PTSitemap,
    'ProductCSitemap': ProductCSitemap,
    'ProductTSitemap': ProductTSitemap,
}

urlpatterns = [
    path('about/', about, name='about'),
    path('contactus/', contactus, name='contactus'),
    path('', home, name='index'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
