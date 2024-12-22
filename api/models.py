from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    ROLE_CHOICES = [
        ('operateur', 'Operateur'),
        ('superviseur', 'Superviseur'),
        ('directeur', 'Directeur'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operateur')

    def __str__(self):
        return self.username


    
class Capteur(models.Model):
    STATES = (
        ('NO_DATA','N/A'),
        ("actif",'Actif'),
        ("enpanne","Enpanne")
    )
    ref = models.CharField(max_length=100,unique=True)
    type = models.CharField(max_length=100,null=True, blank=True)
    unity = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(choices=STATES,max_length=20,default="NO_DATA")
    def __str__(self):
        return self.type

class CapteurData(models.Model):
    STATES = (
        ('NO_DATA','N/A'),
        ("actif",'Actif'),
        ("enpanne","Enpanne")
    )
    capteur = models.ForeignKey(Capteur,on_delete=models.CASCADE,related_name='datas')
    value = models.FloatField()
    state = models.CharField(choices=STATES,max_length=20,default="NO_DATA")
    timestamp = models.DateTimeField(auto_now_add=True)  # Date et heure de l'enregistrement

    def __str__(self):
        return f"Capteur {self.capteur.ref} - {self.state}"
    


class Alert(models.Model):
    user = models.ManyToManyField(User)
    capteur = models.ForeignKey(CapteurData,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
