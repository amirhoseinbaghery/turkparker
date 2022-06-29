from django.contrib import admin

from content.models import About, SocialMedia, ContactUs, SiteSetting, Communication

admin.site.register(About)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = (
        'thumb',
        'title',
        'link',)
    list_display_links = ('thumb', 'title')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'is_read']
    list_filter = ['subject', 'is_read']
    list_editable = ['is_read']
    search_fields = ['name', 'email', 'subject', 'message', 'phone']

    class Meta:
        model = ContactUs


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = (
        'thumb',
        'title',)
    list_display_links = ('thumb', 'title')


@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'phone',
        'tel',)