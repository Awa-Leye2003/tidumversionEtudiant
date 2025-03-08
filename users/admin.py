from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # ✅ Import du modèle utilisateur personnalisé

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')

# ✅ Vérifiez aussi si le groupe Admin est bien enregistré
from django.contrib.auth.models import Group
admin.site.unregister(Group)  # Facultatif, supprime les groupes de l'admin
