from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render

from .serializers import CustomUserSerializer, ProfileSerializer
from .models import CustomUser, Profile


class CustomUserViewSet(viewsets.ModelViewSet):
    """Custom User ViewSet"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """Profile ViewSet"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]