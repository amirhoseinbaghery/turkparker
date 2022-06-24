from django.contrib import admin

from catalog.models import Catalog


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['thumb',
                    'title', ]
    list_display_links = ('thumb', 'title',)
