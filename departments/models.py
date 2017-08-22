# Django
from django.db import models

# Local Django
from departments.variables import REGISTRATIONREQUEST_STATUSES, PENDING


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


class RegistrationRequest(models.Model):
    status = models.PositiveSmallIntegerField(
        verbose_name='Status', choices=REGISTRATIONREQUEST_STATUSES,
        default=PENDING
    )
    create_date = models.DateTimeField(
        verbose_name='Create Date', auto_now_add=True, editable=False
    )
    department = models.ForeignKey(
        verbose_name='Department', to='departments.Department',
        related_name='registration_requests'
    )
    user = models.ForeignKey(
        verbose_name='User', to='users.User',
        related_name='registration_requests'
    )

    class Meta:
        verbose_name = 'Registration Request'
        verbose_name_plural = 'Registration Requests'

    def __str__(self):
        return '{user}'.format(user=self.user.get_full_name())
