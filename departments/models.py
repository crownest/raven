# Django
from django.db import models

# Local Django
from departments.variables import REGISTRATIONREQUEST_STATUSES, PENDING


class Department(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
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
        unique_together = ('name', 'college')

    def __str__(self):
        return '{name} - {college}'.format(
            name=self.name, college=self.college.__str__()
        )


class RegistrationRequest(models.Model):
    email = models.EmailField(verbose_name='Email')
    first_name = models.CharField(verbose_name='First Name', max_length=50)
    last_name = models.CharField(verbose_name='Last Name', max_length=50)
    status = models.PositiveSmallIntegerField(
        verbose_name='Status', choices=REGISTRATIONREQUEST_STATUSES,
        default=PENDING
    )
    create_date = models.DateTimeField(
        verbose_name='Create Date', auto_now_add=True, editable=False
    )
    update_date = models.DateTimeField(
        verbose_name='Update Date', auto_now=True, editable=False
    )
    department = models.ForeignKey(
        verbose_name='Department', to='departments.Department',
        related_name='registration_requests'
    )

    class Meta:
        verbose_name = 'Registration Request'
        verbose_name_plural = 'Registration Requests'
        unique_together = ('email', 'department')

    def __str__(self):
        return '{email} - {department}'.format(
            email=self.email, department=self.department.__str__()
        )

    def _college(self):
        return '{name}'.format(name=self.department.college.name)
    _college.short_description = 'College'
    college = property(_college)
