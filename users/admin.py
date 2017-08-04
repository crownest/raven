# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin

# Local Django
from users.models import User


@admin.register(User)
class UserAdmin(_UserAdmin):

    fieldsets = (
        ('Base Informations', {'fields': ('email', 'password')}),
        ('Personal informations', {
            'fields': (
                'first_name', 'last_name',
                'phone_number', 'college', 'departments'
            ),
            'classes': ('collapse')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser'
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'phone_number',
                'college', 'email', 'password1', 'password2'
            ),
        }),
    )

    list_display = (
        'email', 'first_name', 'last_name',
        'college', 'is_active', 'is_staff', 'is_superuser'
    )
    list_filter = (
        'is_active', 'is_staff', 'is_superuser', 'college', 'departments'
    )
    search_fields = ('email', 'first_name', 'last_name', 'college__name')
    ordering = ('first_name', 'last_name')
