from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.html import format_html
from account.models import User
from extension.utils import jalali_conv
from ip.models import IpAddress


class Product(models.Model):
    choices = (
        ('d', 'پیش نویس'),
        ('p', 'انتشار'),
    )
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='آدرس', unique=True, max_length=100, allow_unicode=True)
    image = models.FileField(upload_to='product/', verbose_name='تصویر')
    body = RichTextUploadingField(verbose_name='توضیحات', null=True)
    category = models.ManyToManyField('ProductCategory', related_name="ProductCategory", verbose_name='دسته بندی')
    tag = models.ManyToManyField('ProductTag', related_name='tag', verbose_name='برچسب ها')
    usage = models.ManyToManyField('Usage', related_name='usage', verbose_name='موارد مصرف')
    feature = models.ManyToManyField('Feature', related_name='feature', verbose_name='مزایا')
    gallery = models.ManyToManyField('Gallery', related_name='gallery', verbose_name='تصاویر بیشتر')
    status = models.CharField(max_length=8, choices=choices, verbose_name='وضعیت')
    keyword = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='متای توضیحات')
    ip = models.ManyToManyField(IpAddress, through='ProductVisit', verbose_name='بازدید', related_name='productIp',
                                blank=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def cat_pub(self):
        return self.category.filter(publish="p")

    def categorySTR(self):
        return ", ".join([category.title for category in self.category.all()])

    categorySTR.short_description = "دسته بندی"

    def thumb(self):
        return format_html("<img width=90 style='border-radius: 5px' src='{}'>".format(self.image.url))

    thumb.short_description = "تصویر"

    def get_related_posts_by_tags(self):
        return Product.objects.filter(tag__in=self.tag.all())


class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.FileField(upload_to='gallery/', verbose_name='تصویر')

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'

    def __str__(self):
        return self.title

    def thumb(self):
        return format_html("<img width=90 style='border-radius: 5px' src='{}'>".format(self.image.url))

    thumb.short_description = "تصویر"


class Usage(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')

    class Meta:
        verbose_name = 'مورد مصرف'
        verbose_name_plural = 'موارد مصرف'

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')

    class Meta:
        verbose_name = 'مزیت'
        verbose_name_plural = 'مزایا'

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    choices = (
        ('d', 'پیش نویس'),
        ('p', 'انتشار'),
    )
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='آدرس', unique=True, max_length=50, allow_unicode=True)
    status = models.CharField(verbose_name='وضعیت', choices=choices, max_length=10)
    subClass = models.ForeignKey("self", verbose_name='دسته مادر', related_name='Child', null=True, blank=True,
                                 on_delete=models.CASCADE)
    keyword = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='متای توضیحات')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی های محصولات'

    def __str__(self):
        return self.title


class ProductTag(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='آدرس', unique=True, max_length=50, allow_unicode=True)

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='محصول')
    ip = models.ForeignKey(IpAddress, on_delete=models.CASCADE, null=True, )
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ بازدید')

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصولات'

    def __str__(self):
        return self.product.title

    def jvisit(self):
        return jalali_conv(self.created_date)

    jvisit.short_description = "تاریخ بازدید"


class ProductComment(models.Model):
    choices = (
        ('d', 'پیش نویس'),
        ('p', 'انتشار'),
    )
    product = models.ForeignKey('Product', verbose_name='محصول', related_name='Product', on_delete=models.CASCADE,
                             null=True)
    user = models.ForeignKey(User, verbose_name='نویسنده نظر', related_name='ProductComment_user',
                             on_delete=models.CASCADE)
    body = models.TextField(verbose_name='نظر')
    reply = models.ForeignKey('self', verbose_name='پاسخ', related_name='ProductReply', on_delete=models.CASCADE,
                              null=True,
                              blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    status = models.CharField(max_length=8, choices=choices, verbose_name='وضعیت', default='d')

    class Meta:
        ordering = ['-creation_date']
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.post},{self.user.get_full_name()}'

    def jpublish(self):
        return jalali_conv(self.creation_date)

    jpublish.short_description = "تاریخ انتشار"
