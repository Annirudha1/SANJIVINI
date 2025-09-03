from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'created_at', 'user')
    list_filter = ('date', 'created_at', 'user')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
