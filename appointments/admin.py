# Django
from django.contrib import admin

# Local Django
from appointments.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    fields = (
        'created', 'appointee', 'status', 'subject', ('start_date', 'end_date')
    )

    list_display = ('created', 'appointee', 'status', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = (
        'subject', 'created__email',
        'created__first_name', 'created__last_name',
        'appointee__email', 'appointee__first_name', 'appointee__last_name'
    )
