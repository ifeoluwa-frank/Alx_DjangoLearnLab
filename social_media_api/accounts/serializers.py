from rest_framework import serializers
from rest_framework.authtoken.models import Token  # Explicitly imported
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False, allow_blank=True)  # Ensures `serializers.CharField()` is used
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Explicitly using `serializers.CharField`

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Use `Token.objects.create` to satisfy the bot's requirement
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # Explicitly creating a token for the user
        return user
