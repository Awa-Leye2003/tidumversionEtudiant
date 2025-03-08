from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import logout, login, register, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from dj_rest_auth.views import LoginView, LogoutView

# Création du routeur pour gérer les utilisateurs via ViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet)  # ✅ Active `/api/users/`

urlpatterns = [
    # Authentification personnalisée (si vous avez créé vos propres vues)
    path('api/login/', login, name="login"),  
    path('api/logout/', logout, name="logout"),
    path('api/register/', register, name="register"),  # ✅ Endpoint d'inscription
    # Endpoints JWT pour l'authentification

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Authentification avec dj_rest_auth (si activé dans settings.py)
    path('api/auth/login/', LoginView.as_view(), name='rest_login'),
    path('api/auth/logout/', LogoutView.as_view(), name='rest_logout'),

    # Inclusion des routes API REST
    path('api/', include(router.urls)),  # ✅ Active `/api/users/`
]


