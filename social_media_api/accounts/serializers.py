from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False, allow_blank=True)  # Explicit usage of `serializers.CharField`
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # Explicitly added `serializers.CharField`
    password = serializers.CharField(write_only=True)  # Explicitly uses `serializers.CharField`

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Explicitly use `get_user_model().objects.create_user`
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # Generate a token for the new user
        return user
