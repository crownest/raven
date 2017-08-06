# Django
from django.contrib import admin
# Local Django
from sparetimes.models import SpareTime

@admin.register(SpareTime)
class SpareTime±Admin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'user')
    list_filter = ('user',)
    search_fields = ('user',)
