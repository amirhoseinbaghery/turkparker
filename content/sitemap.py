from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Blog, BlogCategory, BlogTag
from product.models import Product, ProductCategory, ProductTag
from project.models import Project, ProjectCategory, ProjectTag


class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.filter(status='p')

    def lastmod(self, obj):
        return obj.updatedDate


class BCSitemap(Sitemap):
    def items(self):
        return BlogCategory.objects.all()


class BTSitemap(Sitemap):
    def items(self):
        return BlogTag.objects.all()


class ProjectSitemap(Sitemap):
    def items(self):
        return Project.objects.filter(status='p')


class PCSitemap(Sitemap):
    def items(self):
        return ProjectCategory.objects.all()


class PTSitemap(Sitemap):
    def items(self):
        return ProjectTag.objects.all()


class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.filter(status='p')


class ProductCSitemap(Sitemap):
    def items(self):
        return ProductCategory.objects.all()


class ProductTSitemap(Sitemap):
    def items(self):
        return ProductTag.objects.all()


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['content:contactus', 'content:index', 'content:about', 'catalog:List']

    def location(self, item):
        return reverse(item)
