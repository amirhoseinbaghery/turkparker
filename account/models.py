from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='شماره موبایل')
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name='استان')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='شهر')
    bio = models.TextField(blank=True, null=True, verbose_name='بیوگرافی')
    image = models.ImageField(blank=True, null=True, verbose_name='تصویر پروفایل')