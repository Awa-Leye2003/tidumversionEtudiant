from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Inclure les routes pour les assets, ports, applications...
    path('api/', include('assets.urls')),  
    path('api/', include('users.urls')), 
   
    # ✅ Authentification Django REST Framework
    path('api/auth/', include('rest_framework.urls')),  # Pour login/logout via l'interface DRF

    # ✅ Authentification avec `dj-rest-auth`
    path('api/auth/', include('dj_rest_auth.urls')),  

    # ✅ Inscription des utilisateurs avec `dj-rest-auth` et `allauth`
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')), 

]



   

