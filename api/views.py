from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Alert, CapteurData,Capteur
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializers import AlertSerializer, UserSerializer, CapteurDataSerializer,CapteurSerializer
from django.contrib.auth.decorators import login_required
from .models import User  # Importez le modèle User

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



from django.shortcuts import render



class Dashboard(View):
    template_name= "index.html"
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        context = {"title" : 'ANDON 4.0'}
        return render(request, self.template_name,context)



class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            return render(request, self.template_name)
        

class TableView(View):
    template_name = 'table-basic.html'

    def get(self, request, *args, **kwargs):
        context = {'capteur_data' : CapteurData.objects.all().order_by('-pk')}
        print(context)
        return render(request, self.template_name,context)

@login_required
def profile_view(request):
    user = request.user
    countries = ["London", "India", "USA", "Canada", "Thailand"]

    if request.method == "POST":
        user.first_name = request.POST.get("full_name").split(" ")[0]
        user.last_name = " ".join(request.POST.get("full_name").split(" ")[1:])
        user.email = request.POST.get("email")
        user.phone_number = request.POST.get("phone_number")
        user.role = request.POST.get("role")
        user.save()
        # Message de confirmation si besoin
        messages.success(request, "Profile updated successfully!")

    return render(request, 'profile.html', {"user": user, "countries": countries})

def alert_view(request):
    # Récupérer toutes les alertes
    alerts = Alert.objects.all()
    return render(request, 'index.html', {'alerts': alerts})

def alert_list_view(request):
    # Récupérer toutes les alertes de la base de données
    alerts = Alert.objects.all()
    # Passer les alertes au template
    return render(request, 'alert.html', {'alerts': alerts})



def user_list_view(request):
    # Récupérer tous les utilisateurs
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
