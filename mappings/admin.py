from django.contrib import admin
from .models import PatientDoctorMapping

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'appointment_date', 'created_at']
    list_filter = ['appointment_date', 'created_at']