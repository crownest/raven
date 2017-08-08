# Django
from django.contrib import admin

# Local Django
from departments.models import Department, RegistrationRequest


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(RegistrationRequest)
class RegistrationRequestAdmin(admin.ModelAdmin):
    fields = ('status', 'user', 'department', 'create_date')
    readonly_fields = ('create_date',)

    list_display = ('status', 'user', 'department', 'create_date')
    list_filter = ('status', 'create_date')
    search_fields = (
        'user__email', 'user__first_name',
        'user__last_name', 'department__name'
    )
