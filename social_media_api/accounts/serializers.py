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


class GraderUserSerializer(serializers.Serializer):
    password = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ['username', 'email','password']

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        token = Token.objects.create(user=user)
        return user, token

