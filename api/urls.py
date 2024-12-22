from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlertViewSet, UserViewSet, CapteurDataViewSet

# Création d'un routeur pour gérer automatiquement les routes des API
router = DefaultRouter()
router.register(r'alerts', AlertViewSet ) # Endpoint pour les alertes
router.register(r'users', UserViewSet)  # Endpoint pour les utilisateurs
router.register(r'capteur-data', CapteurDataViewSet) 
# Routes finales
urlpatterns = [
    path('', include(router.urls)),  # Inclure toutes les routes du routeur
]
