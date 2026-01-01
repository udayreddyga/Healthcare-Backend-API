from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'specialization', 'created_at']
    search_fields = ['name', 'email', 'specialization']
    list_filter = ['specialization', 'created_at']