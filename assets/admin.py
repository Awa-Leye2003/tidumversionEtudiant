from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Asset, Port, Application, WebMetadata

# Enregistrer les modèles pour les voir dans l'admin
admin.site.register(Asset)
admin.site.register(Port)
admin.site.register(Application)
admin.site.register(WebMetadata)
