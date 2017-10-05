# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin

# Local Django
from users.models import User, SpareTime


@admin.register(User)
class UserAdmin(_UserAdmin):

    fieldsets = (
        ('Base Informations', {'fields': ('user_type', 'email', 'password')}),
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


@admin.register(SpareTime)
class SpareTimeAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'user')
    list_filter = ('start_date', 'end_date')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
