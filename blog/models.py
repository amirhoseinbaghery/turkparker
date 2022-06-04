from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from ip.models import IpAddress
from account.models import User
from extension.utils import jalali_conv
import readtime


class Blog(models.Model):
    choices = (
        ('d', 'پیش نویس'),
        ('p', 'انتشار'),
    )
    title = models.CharField(verbose_name='عنوان', max_length=50)
    slug = models.SlugField(verbose_name='آدرس', unique=True, max_length=100, allow_unicode=True)
    author = models.ForeignKey(User, verbose_name='نویسنده', on_delete=models.SET_NULL, null=True,
                               related_name='author')
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ')
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updatedDate = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    status = models.CharField(max_length=8, choices=choices, verbose_name='وضعیت')
    keyword = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='متای توضیحات')
    image = models.ImageField(upload_to='blog/', verbose_name='تصویر', null=True)
    body = RichTextUploadingField(verbose_name='متن مقاله', null=True)
    category = models.ManyToManyField('BlogCategory', related_name="Category", verbose_name='دسته بندی')
    similar_category = models.ForeignKey('BlogCategory', on_delete=models.SET_NULL, null=True,
                                         related_name='similar_category', verbose_name='دسته بندی اصلی')
    tag = models.ManyToManyField('BlogTag', related_name='tag', verbose_name='برچسب ها')
    ip = models.ManyToManyField(IpAddress, through='PostVisit', verbose_name='بازدید', related_name='blogIp',
                                blank=True)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def cat_pub(self):
        return self.category.filter(publish="p")

    def categorySTR(self):
        return ", ".join([category.title for category in self.category.all()])

    categorySTR.short_description = "دسته بندی"

    def jpublish(self):
        return jalali_conv(self.publish)

    jpublish.short_description = "تاریخ انتشار"

    def jupdatedDate(self):
        return jalali_conv(self.updatedDate)

    jpublish.short_description = "تاریخ بروزرسانی"

    def thumb(self):
        return format_html("<img width=90 style='border-radius: 5px' src='{}'>".format(self.image.url))

    thumb.short_description = "تصویر"

    def get_absolute_url(self):
        return reverse('blog:SinglePost', kwargs={'Slug': self.slug})

    def get_readtime(self):
        result = readtime.of_text(self.body)
        return result.text

    get_readtime.short_description = "زمان مطالعه"

    def get_related_posts_by_tags(self):
        return Blog.objects.filter(tag__in=self.tag.all())


class BlogCategory(models.Model):
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
        verbose_name_plural = 'دسته بندی های مقالات'

    def __str__(self):
        return self.title


class BlogTag(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='آدرس', unique=True, max_length=50, allow_unicode=True)

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    choices = (
        ('d', 'پیش نویس'),
        ('p', 'انتشار'),
    )
    post = models.ForeignKey('Blog', verbose_name='مقاله', related_name='Post', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, verbose_name='نویسنده نظر', related_name='blogcomment_user',
                             on_delete=models.CASCADE)
    body = models.TextField(verbose_name='نظر')
    reply = models.ForeignKey('self', verbose_name='پاسخ', related_name='Reply', on_delete=models.CASCADE, null=True,
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


class PostVisit(models.Model):
    article = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, verbose_name='مقاله')
    ip = models.ForeignKey(IpAddress, on_delete=models.CASCADE, null=True, verbose_name='')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ بازدید')

    class Meta:
        verbose_name = 'بازدید مقاله'
        verbose_name_plural = 'بازدید های مقالات'

    def __str__(self):
        return self.article.title

    def jvisit(self):
        return jalali_conv(self.created_date)

    jvisit.short_description = "تاریخ بازدید"
