from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Alert, CapteurData,Capteur
from .serializers import AlertSerializer, UserSerializer, CapteurDataSerializer,CapteurSerializer

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


class CapteurViewSet(viewsets.ModelViewSet):
    queryset = Capteur.objects.all()
    serializer_class = CapteurSerializer


