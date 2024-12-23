from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Alert, CapteurData,Capteur

# Récupérer le modèle utilisateur personnalisé
User = get_user_model()

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'



class CapteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capteur
        fields = '__all__'

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role']

class CapteurDataSerializer(serializers.ModelSerializer):
    info_capteur = serializers.SerializerMethodField()
    class Meta:
        model = CapteurData
        fields = '__all__'

    def get_info_capteur(self,obj):
        return obj.capteur.ref