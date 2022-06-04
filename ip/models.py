from django.db import models


class IpAddress(models.Model):
    ip = models.GenericIPAddressField(verbose_name='آدرس ip')

    def __str__(self):
        return self.ip
