# Django
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

# Local Django
from users.managers import UserManager
from users.variables import USER_TYPES, DEFAULT


class User(AbstractBaseUser, PermissionsMixin):
    user_type = models.PositiveSmallIntegerField(
	   verbose_name='User Type', choices=USER_TYPES, default=DEFAULT
    )
    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=50)
    last_name = models.CharField(verbose_name='Last Name', max_length=50)
    phone_number = models.CharField(
        verbose_name='Phone Number', max_length=50, blank=True
    )
    is_active = models.BooleanField(verbose_name=('Active'), default=True)
    is_staff = models.BooleanField(verbose_name=('Staff'), default=False)
    college = models.ForeignKey(
        verbose_name='College', to='colleges.College',
        related_name='users', null=True
    )
    departments = models.ManyToManyField(
        verbose_name='Department', to='departments.Department',
        related_name='users', blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.get_short_name()

    def get_short_name(self):
        return '{first_name}'.format(first_name=self.first_name)

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )


class SpareTime(models.Model):
    start_date = models.DateTimeField(verbose_name='Start date')
    end_date = models.DateTimeField(verbose_name='End date')
    user = models.ForeignKey(
        verbose_name='User', to='users.User', related_name='spare_times'
    )
    
    class Meta:
        verbose_name = 'Spare Time'
        verbose_name_plural = 'Spare Times'

    def __str__(self):
        return '{start_date} - {end_date}'.format(
            start_date=self.start_date, end_date=self.end_date
        )
