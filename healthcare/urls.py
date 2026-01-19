from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.authtoken import views as auth_views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_token(request):
    from rest_framework.authtoken.models import Token
    token, created = Token.objects.get_or_create(user=request.user)
    return Response({'token': token.key})


def home(request):
    return JsonResponse({"status": "Healthcare API is live"})


urlpatterns = [
    path('', home),

    path('api/doctors/', include('doctors.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/mappings/', include('mappings.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
    path('api/my-token/', get_my_token, name='my_token'),
]
