from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.get('role', 'scanner')  # 📌 Rôle par défaut = scanner

        # Empêcher un utilisateur normal de créer un admin
        if role == 'admin' and not self.context['request'].user.is_superuser:
            raise serializers.ValidationError({"role": "Seul un admin peut créer un autre admin."})

        user = User.objects.create_user(**validated_data)  # 📌 Création avec mot de passe sécurisé
        return user
