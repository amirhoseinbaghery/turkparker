from django.db import models
from django.utils.html import format_html


class Catalog(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    image = models.ImageField(upload_to='catalog/', verbose_name='تصویر')
    file = models.FileField(upload_to='catalog/', verbose_name='کاتالوگ')


    class Meta:
        verbose_name = 'کاتالوگ'
        verbose_name_plural = 'کاتالوگ ها'

    def __str__(self):
        return self.title

    def thumb(self):
        return format_html("<img width=90 style='border-radius: 5px' src='{}'>".format(self.image.url))

    thumb.short_description = "تصویر"