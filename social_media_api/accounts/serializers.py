from rest_framework import serializers
from django.contrib.auth import get_user_model

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



