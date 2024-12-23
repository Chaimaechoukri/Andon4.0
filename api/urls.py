from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlertViewSet, LoginView, UserViewSet, CapteurDataViewSet,CapteurViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  AlertViewSet, UserViewSet, CapteurViewSet, CapteurDataViewSet,Dashboard,TableView
from django.views.generic import TemplateView
# Création d'un routeur pour gérer automatiquement les routes des API
router = DefaultRouter()
router.register(r'alerts', AlertViewSet)  # Endpoint pour les alertes
router.register(r'users', UserViewSet)  # Endpoint pour les utilisateurs
router.register(r'capteur', CapteurViewSet)  # Endpoint pour les capteurs
router.register(r'capteur-data', CapteurDataViewSet)  # Endpoint pour les données des capteurs

# Routes finales
urlpatterns = [
    path('', Dashboard.as_view(), name='index'),
    path('login/',LoginView.as_view() , name='login'),
    path('profile/', TemplateView.as_view(template_name='pages-profile.html'), name='profile'),
    path('table/', TableView.as_view(), name='table'),
    # Route pour les API (préfixée par `/api/`)
    path('api/', include(router.urls)),  

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
