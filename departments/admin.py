# Django
from django.contrib import admin
# Local Django
from departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    list_filter = ('name',)
    search_fields = ('name',)
