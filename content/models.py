from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.html import format_html

from account.models import User


class About(models.Model):
    our_team = models.ManyToManyField(User, verbose_name='تیم ما', related_name='ourTeam')
    image = models.ImageField(null=True, blank=True, verbose_name='تصویر')
    body = RichTextUploadingField(verbose_name='متن درباره ما', null=True)
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='متای توضیحات')
    keyword = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, blank=True)
    social_media = models.ManyToManyField('SocialMedia', verbose_name='شبکه های اجتماعی', related_name='SocialMedia')
    admin_message = models.CharField(max_length=900, verbose_name='پیام مدیر', null=True)
    history = models.IntegerField(verbose_name='سابقه کاری', null=True)

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'


class SocialMedia(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    link = models.CharField(max_length=300, verbose_name='لینک')
    image = models.FileField(upload_to='social/', verbose_name='آیکون شبکه اجتماعی')

    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'

    def __str__(self):
        return self.title

    def thumb(self):
        return format_html("<img width=90 style='border-radius: 5px' src='{}'>".format(self.image.url))

    thumb.short_description = "تصویر"


class ContactUs(models.Model):
    choice = (
        ('پشتیبانی سایت', 'پشتیبانی سایت'),
        ('انتقادات و پیشنهادات', 'انتقادات و پیشنهادات'),
        ('پیگیری سفارش', 'پیگیری سفارش'),
        ('پشتیبانی محصول', 'پشتیبانی محصول'),
        ('مدیریت', 'مدیریت'),
        ('حسابداری و امورمالی ', 'حسابداری و امورمالی'),
        ('سایر موضوعات', 'سایر موضوعات'),
    )
    subject = models.CharField(max_length=50, null=True, choices=choice, verbose_name='موضوع')
    name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='تلفن تماس')
    message = models.TextField(verbose_name='متن پیام')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده")

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.subject


class SiteSetting(models.Model):
    image = models.FileField(upload_to='site_setting/', verbose_name='عکس')
    title = models.CharField(max_length=50, verbose_name='عنوان', null=True)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.title

    def thumb(self):
        return format_html("<img width=90 style='border-radius: 5px' src='{}'>".format(self.image.url))

    thumb.short_description = "تصویر"


class Communication(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='همراه')
    tel = models.CharField(max_length=11, verbose_name='تلفن تماس')
    fax = models.CharField(max_length=11, verbose_name='فکس', null=True)
    staff = models.CharField(max_length=11, verbose_name='کارشناس', null=True)
    staff1 = models.CharField(max_length=11, verbose_name='کارشناس', null=True)
    address = models.CharField(max_length=100, verbose_name='آدرس دفتر')
    address1 = models.CharField(max_length=100, null=True, verbose_name='آدرس کارخانه')

    class Meta:
        verbose_name = 'ارتباط'
        verbose_name_plural = 'ارتباطات'

    def __str__(self):
        return self.email
