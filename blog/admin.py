from django.contrib import admin

from blog.models import Blog, BlogTag, BlogCategory, BlogComment, PostVisit


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'thumb',
        'title',
        'author',
        'jpublish',
        'status',
        'categorySTR',)

    list_display_links = ('thumb', 'title')
    list_filter = ('author',
                   'status')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'body']
    list_editable = ('status', 'author',)


admin.site.register(Blog, BlogAdmin)


class AdminBlogTag(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'slug']


admin.site.register(BlogTag, AdminBlogTag)


class AdminBlogCategory(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'status',
        'subClass',)
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('status',)


admin.site.register(BlogCategory, AdminBlogCategory)


class AdminBlogComment(admin.ModelAdmin):
    list_display = (
        'post',
        'user',
        'jpublish',
        'status',
        'body',
        'reply',)

    list_filter = ('post',
                   'user',
                   'status')
    search_fields = ['reply', 'body']
    list_editable = ('status',)


admin.site.register(BlogComment, AdminBlogComment)


@admin.register(PostVisit)
class PostVisitAdmin(admin.ModelAdmin):
    list_display = ['article',
                    'ip',
                    'jvisit', ]
    list_filter = ['article',
                   'ip', ]
