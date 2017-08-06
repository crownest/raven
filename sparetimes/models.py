# Django
from django.db import models

class SpareTime(models.Model):
    start_date- = models.DateTimeField(verbose_name='Start date')
    end_date = models.DateTimeField(verbose_name="End date")
    user = models.ForeingKey(verbose_name="User", to='users.User',related_name='spare_times')

    class Meta:
        verbose_name = 'Spare Time'
        verbose_name_plural = 'Spare Times'

    def __str__(self):
        return '{start_date}'.format(start_date=self.start_date)
