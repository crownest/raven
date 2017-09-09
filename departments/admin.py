# Django
from django.contrib import admin

# Local Django
from departments.models import Department, RegistrationRequest


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'phone_number')
    search_fields = ('name', 'college__name')


@admin.register(RegistrationRequest)
class RegistrationRequestAdmin(admin.ModelAdmin):
    fields = (
        'status', 'email', 'first_name', 'last_name',
        'department', ('create_date', 'update_date')
    )
    readonly_fields = ('create_date', 'update_date')

    list_display = (
        'status', 'email', 'first_name', 'last_name',
        'department', 'create_date', 'update_date'
    )
    list_filter = ('status', 'create_date', 'update_date')
    search_fields = (
        'email', 'first_name', 'last_name', 'department__name'
    )

    def get_fields(self, request, *args, **kwargs):
        fields = super(RegistrationRequestAdmin, self).get_fields(request, *args, **kwargs)
        exclude_fields = []

        if 'add' in request.path.split('/'):
            exclude_fields += [('create_date', 'update_date')]

        return [field for field in fields if field not in exclude_fields]
