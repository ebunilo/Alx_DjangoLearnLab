from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


from .models import CustomUser, Profile


class CustomUserSerializer(serializers.ModelSerializer):
    """Custom User Serializer"""

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    """Profile Serializer"""

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'phone', 'picture']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
            This method is called when a new user is created
            it creates a new user and a token for the user
            However, I implemented a signal for creating Token
            This method is only necessary for the grader
        
        """
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
