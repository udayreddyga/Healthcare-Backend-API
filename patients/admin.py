from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'age', 'gender', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['gender', 'age', 'created_at']