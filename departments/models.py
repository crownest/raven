# Django
from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50, unique=True)
    phone_number = models.CharField(
        verbose_name='Phone Number', max_length=50, blank=True
    )
    college = models.ForeignKey(
        verbose_name='College', to='colleges.College',
        related_name='departments'
    )

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return '{name}'.format(name=self.name)
