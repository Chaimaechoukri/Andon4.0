from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Alert, CapteurData,Capteur
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
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

