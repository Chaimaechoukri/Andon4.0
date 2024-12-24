from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from . import views  # Assurez-vous que l'importation de views est correcte
from .views import AlertViewSet, LoginView, UserViewSet, CapteurDataViewSet, CapteurViewSet
from .views import alert_list_view  # Assure-toi que la vue est bien importée
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


# Création d'un routeur pour gérer automatiquement les routes des API
router = DefaultRouter()
router.register(r'alerts', AlertViewSet)  # Endpoint pour les alertes
router.register(r'users', UserViewSet)  # Endpoint pour les utilisateurs
router.register(r'capteur', CapteurViewSet)  # Endpoint pour les capteurs
router.register(r'capteur-data', CapteurDataViewSet)  # Endpoint pour les données des capteurs

# Routes finales
urlpatterns = [
                  path('', views.Dashboard.as_view(), name='index'),  # Accéder à la page d'accueil
                  path('login/', views.LoginView.as_view(), name='login'),  # Page de connexion
                  path('profile/', TemplateView.as_view(template_name='pages-profile.html'), name='profile'),  # Profil de l'utilisateur
                  path('table/', views.TableView.as_view(), name='table'),  # Page de tableau
                  path('alerts/', alert_list_view, name='alerts'),  # URL pour la liste des alertes
                  path('api/visitor-data/', views.get_visitor_data, name='get_visitor_data'),
                  path('users/', views.user_list_view, name='users'),  # Route vers la vue de la liste des utilisateurs
                  # Routes de l'API
                  path('api/', include(router.urls)),  # Routes pour l'API
                  path('login/',LogoutView.as_view(next_page='/login/'), name='logout'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
