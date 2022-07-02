from django.contrib import admin

from product.models import ProductVisit, ProductCategory, ProductTag, ProductComment, Product, Gallery, Feature, Usage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'thumb',
        'title',
        'slug',
        'status',)

    list_display_links = ('thumb', 'title')
    list_filter = ('status',)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'body']
    list_editable = ('status',)


@admin.register(Gallery)
class CostumerAdmin(admin.ModelAdmin):
    list_display = ['thumb',
                    'title', ]
    list_display_links = ['thumb',
                          'title', ]


@admin.register(ProductTag)
class AdminProductTag(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'slug']


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    list_display = (
        'thumb',
        'title',
        'slug',
        'status',
        'subClass',)
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('status',)


@admin.register(ProductComment)
class AdminProductComment(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'jpublish',
        'status',
        'body',
        'reply',)

    list_filter = ('product',
                   'user',
                   'status')
    search_fields = ['reply', 'body']
    list_editable = ('status',)


@admin.register(ProductVisit)
class ProductVisitAdmin(admin.ModelAdmin):
    list_display = ['product',
                    'ip',
                    'jvisit', ]
    list_filter = ['product',
                   'ip', ]


admin.site.register(Usage)
admin.site.register(Feature)
