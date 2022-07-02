from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html

from account.models import User
from costumer.models import Costumer
from extension.utils import jalali_conv
from ip.models import IpAddress


class Project(models.Model):
    choices = (
        ('d', 'پیش نویس'),
        ('p', 'انتشار'),
    )
    title = models.CharField(verbose_name='عنوان', max_length=50)
    slug = models.SlugField(verbose_name='آدرس', unique=True, max_length=100, allow_unicode=True)
    startDate = models.DateTimeField(verbose_name='تاریخ شروع', null=True, blank=True)
    endDate = models.DateTimeField(verbose_name='تاریخ پایان', null=True, blank=True)
    status = models.CharField(max_length=8, choices=choices, verbose_name='وضعیت')
    keyword = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='متای توضیحات')
    image = models.ImageField(upload_to='project/', verbose_name='تصویر', null=True)
    body = RichTextUploadingField(verbose_name='متن پروژه', null=True)
    category = models.ManyToManyField('ProjectCategory', related_name="ProjectCategory", verbose_name='دسته بندی')
    tag = models.ManyToManyField('ProjectTag', related_name='ProjectTag', verbose_name='برچسب ها')
    gallery = models.ManyToManyField('ProjectGallery', related_name='ProjectGallery', verbose_name='گالری')
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='Costumer', null=True,
                                 verbose_name='مشتری')
    ip = models.ManyToManyField(IpAddress, through='ProjectVisit', verbose_name='بازدید', related_name='ProjectIp',
                                blank=True)

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'
        ordering = ['-startDate']

    def __str__(self):
        return self.title

    def cat_pub(self):
        return self.category.filter(publish="p")

    def jstart(self):
        return jalali_conv(self.startDate)

    jstart.short_description = "تاریخ شروع"

    def jend(self):
        return jalali_conv(self.endDate)

    jend.short_description = "تاریخ شروع"

    def categorySTR(self):
        return ", ".join([category.title for category in self.category.all()])

    categorySTR.short_description = "دسته بندی"

    def thumb(self):
        return format_html("<img width=90 style='border-radius: 5px' src='{}'>".format(self.image.url))

    thumb.short_description = "تصویر"

    def get_absolute_url(self):
        return reverse('project:Project', kwargs={'slug': self.slug})

    def get_related_posts_by_tags(self):
        return Project.objects.filter(tag__in=self.tag.all())


class ProjectCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='آدرس', unique=True, max_length=50, allow_unicode=True)
    subClass = models.ForeignKey("self", verbose_name='دسته مادر', related_name='ProjectChild', null=True, blank=True,
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/category/', verbose_name='تصویر', null=True)
    keyword = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='متای توضیحات')
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی های پروژه ها'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project:CategoryList', kwargs={'slug': self.slug})


class ProjectTag(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='آدرس', unique=True, max_length=50, allow_unicode=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ')
    keyword = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='متای توضیحات')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project:tagList', kwargs={'slug': self.slug})


class ProjectComment(models.Model):
    choices = (
        ('d', 'پیش نویس'),
        ('p', 'انتشار'),
    )
    project = models.ForeignKey('Project', verbose_name='پروژه', related_name='Project', on_delete=models.CASCADE,
                                null=True)
    user = models.ForeignKey(User, verbose_name='نویسنده نظر', related_name='ProjectComment',
                             on_delete=models.CASCADE)
    body = models.TextField(verbose_name='نظر')
    reply = models.ForeignKey('self', verbose_name='پاسخ', related_name='ProjectReply', on_delete=models.CASCADE,
                              null=True,
                              blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    status = models.CharField(max_length=8, choices=choices, verbose_name='وضعیت', default='d')

    class Meta:
        ordering = ['-creation_date']
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.project},{self.user.get_full_name()}'

    def jpublish(self):
        return jalali_conv(self.creation_date)

    jpublish.short_description = "تاریخ انتشار"


class ProjectVisit(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, verbose_name='پروژه')
    ip = models.ForeignKey(IpAddress, on_delete=models.CASCADE, null=True, verbose_name='')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ بازدید')

    class Meta:
        verbose_name = 'بازدید پروژه'
        verbose_name_plural = 'بازدید های پروژه ها'

    def __str__(self):
        return self.project.title

    def jvisit(self):
        return jalali_conv(self.created_date)

    jvisit.short_description = "تاریخ بازدید"


class ProjectGallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.FileField(upload_to='projectGallery/', verbose_name='تصویر')

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'

    def __str__(self):
        return self.title

    def thumb(self):
        return format_html("<img width=90 style='border-radius: 5px' src='{}'>".format(self.image.url))

    thumb.short_description = "تصویر"
