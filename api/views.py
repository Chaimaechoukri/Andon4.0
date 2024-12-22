from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Alert, CapteurData
from .serializers import AlertSerializer, UserSerializer, CapteurDataSerializer

# Récupérer le modèle utilisateur personnalisé
User = get_user_model()

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CapteurDataViewSet(viewsets.ModelViewSet):
    queryset = CapteurData.objects.all()
    serializer_class = CapteurDataSerializer