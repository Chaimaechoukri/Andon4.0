from django.contrib import admin
from .models import User, Capteur, CapteurData, Alert
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'role')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')

@admin.register(Capteur)
class CapteurAdmin(admin.ModelAdmin):
    list_display = ('ref', 'type', 'unity', 'state')
    list_filter = ('state', 'type')
    search_fields = ('ref', 'type', 'unity')

@admin.register(CapteurData)
class CapteurDataAdmin(admin.ModelAdmin):
    list_display = ('capteur', 'value', 'state', 'timestamp')
    list_filter = ('state', 'timestamp')
    search_fields = ('capteur__ref',)

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'capteur', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('title', 'description')
    filter_horizontal = ('user',)
