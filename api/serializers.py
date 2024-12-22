from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Alert, CapteurData

# Récupérer le modèle utilisateur personnalisé
User = get_user_model()

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role']

class CapteurDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapteurData
        fields = '__all__'
