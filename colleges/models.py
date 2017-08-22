# Django
from django.db import models


class College(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50, unique=True)
    address = models.TextField(verbose_name='Address', blank=True)
    phone_number = models.CharField(
        verbose_name='Phone Number', max_length=50, blank=True
    )

    class Meta:
        verbose_name = 'College'
        verbose_name_plural = 'Colleges'

    def __str__(self):
        return '{name}'.format(name=self.name)
