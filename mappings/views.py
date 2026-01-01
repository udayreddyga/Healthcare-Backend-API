from rest_framework import viewsets, permissions
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    