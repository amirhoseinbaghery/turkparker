from django.contrib import admin

from costumer.models import Costumer, Locality


@admin.register(Costumer)
class CostumerAdmin(admin.ModelAdmin):
    list_display = ['thumb',
                    'name', ]
    list_display_links = ['thumb',
                          'name', ]


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ['country',
                    'city', ]
    list_display_links = ['country',
                          'city', ]
