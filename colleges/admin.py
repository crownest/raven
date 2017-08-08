# Django
from django.contrib import admin

# Local Django
from colleges.models import College


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    list_filter = ('name',)
    search_fields = ('name',)
