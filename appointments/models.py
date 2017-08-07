# Django
from django.db import models

# Local Django
from appointments.variables import APPOINTMENT_STATUSES, PENDING


class Appointment(models.Model):
    status = models.PositiveSmallIntegerField(
        verbose_name='Status', choices=APPOINTMENT_STATUSES, default=PENDING
    )
    subject = models.TextField(verbose_name='Subject')
    start_date = models.DateTimeField(verbose_name='Start Date')
    end_date = models.DateTimeField(verbose_name='End Date')
    created = models.ForeignKey(
        verbose_name='Created', to='users.User'
    )
    appointee = models.ForeignKey(
        verbose_name='Appointee', to='users.User', related_name='appointments'
    )

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return '{created} - {appointee}'.format(
            created=self.created.get_full_name(),
            appointee=self.appointee.get_full_name()
        )
