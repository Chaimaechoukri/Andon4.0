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
from django.db.models import Count, Q
from django.http import JsonResponse
from .models import Capteur, CapteurData

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



def get_capteur_data(request):
    # Récupération des données des capteurs
    capteurs = Capteur.objects.all()
    data = []
    for capteur in capteurs:
        latest_data = capteur.datas.order_by('-timestamp').first()  # Dernière valeur enregistrée
        data.append({
            'ref': capteur.ref,
            'type': capteur.type,
            'value': latest_data.value if latest_data else None,  # Valeur si existante
        })
    return JsonResponse(data, safe=False)


from .models import Capteur, CapteurData

def get_visitor_data(request):
    capteurs = Capteur.objects.all()
    data = []

    for capteur in capteurs:
        total_entries = capteur.datas.count()  # Nombre total d'enregistrements
        enpanne_count = capteur.datas.filter(state="enpanne").count()  # Nombre d'enregistrements en état "enpanne"

        if total_entries > 0:
            enpanne_percentage = (enpanne_count / total_entries) * 100
        else:
            enpanne_percentage = 0  # Si aucun enregistrement, le pourcentage est 0

        data.append({
            "ref": capteur.ref,
            "percentage": enpanne_percentage
        })

    return JsonResponse(data, safe=False)


