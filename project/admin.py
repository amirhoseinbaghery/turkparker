from django.contrib import admin
from .models import Project, ProjectCategory, ProjectTag, ProjectComment, ProjectVisit, ProjectGallery


class projectAdmin(admin.ModelAdmin):
    list_display = (
        'thumb',
        'title',
        'status',
        'categorySTR',)

    list_display_links = ('thumb', 'title')
    list_filter = ('status',)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'body']
    list_editable = ('status',)


admin.site.register(Project, projectAdmin)


class AdminprojectTag(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'slug']


admin.site.register(ProjectTag, AdminprojectTag)


class AdminprojectCategory(admin.ModelAdmin):
    list_display = ('title',
                    'slug',
                    'subClass',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ProjectCategory, AdminprojectCategory)


class AdminprojectComment(admin.ModelAdmin):
    list_display = (
        'project',
        'user',
        'jpublish',
        'status',
        'body',
        'reply',)

    list_filter = ('project',
                   'user',
                   'status')
    search_fields = ['reply', 'body']
    list_editable = ('status',)


admin.site.register(ProjectComment, AdminprojectComment)


@admin.register(ProjectVisit)
class projectVisitAdmin(admin.ModelAdmin):
    list_display = ['project',
                    'ip',
                    'jvisit', ]
    list_filter = ['project',
                   'ip', ]


admin.site.register(ProjectGallery)
