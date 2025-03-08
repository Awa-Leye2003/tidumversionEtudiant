from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import UserSerializer

User = get_user_model()  # ✅ Utilise le modèle personnalisé


# ✅ VueSet pour la gestion des utilisateurs (Admin uniquement)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Seuls les admins peuvent voir/modifier les utilisateurs

# ✅ Endpoint pour la connexion d'un utilisateur
@api_view(['POST'])
@permission_classes([AllowAny])  # Accessible par tout le monde
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Veuillez fournir un nom d'utilisateur et un mot de passe."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.id, "role": user.role})

    return Response({"error": "Nom d'utilisateur ou mot de passe incorrect."}, status=status.HTTP_401_UNAUTHORIZED)

# ✅ Endpoint pour l'inscription d'un utilisateur (Seul un admin peut créer un autre admin)
@api_view(['POST'])
@permission_classes([AllowAny])  
def register(request):
    serializer = UserSerializer(data=request.data, context={'request': request})
    
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.id, "role": user.role}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Endpoint pour la déconnexion d'un utilisateur
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Seuls les utilisateurs connectés peuvent se déconnecter
def logout(request):
    try:
        request.user.auth_token.delete()  # Supprime le token d'authentification
        return Response({"message": "Déconnexion réussie."}, status=200)
    except:
        return Response({"error": "Erreur lors de la déconnexion."}, status=500)
