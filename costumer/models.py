from django.db import models
from django.utils.html import format_html


class Costumer(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام مشتری/شرکت')
    image = models.FileField(upload_to='costumer/', verbose_name='لوگو')
    location = models.ForeignKey('Locality', verbose_name='موقعییت مشتری', on_delete=models.CASCADE,
                                 related_name='costumer', null=True)

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    def __str__(self):
        return self.name

    def thumb(self):
        return format_html("<img width=90 style='border-radius: 5px' src='{}'>".format(self.image.url))

    thumb.short_description = "تصویر"


class Locality(models.Model):
    country = models.CharField(max_length=100, verbose_name='کشور', default='ایران')
    city = models.CharField(max_length=100, verbose_name='شهر')

    class Meta:
        verbose_name = 'موقعیت مشتری'
        verbose_name_plural = 'موقعیت مشتری ها'

    def __str__(self):
        return f"{self.country} {self.city}"
