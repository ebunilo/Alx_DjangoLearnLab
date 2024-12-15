from rest_framework import viewsets
from rest_framework import permissions, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from .serializers import CustomUserSerializer, ProfileSerializer, RegisterSerializer
from .models import CustomUser, Profile


class CustomUserViewSet(viewsets.ModelViewSet):
    """Custom User ViewSet"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """Profile ViewSet"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({"token": token.key, "user_id": token.user_id})

#! Ignore 
from accounts.models import CustomUser
from rest_framework.response import Response
class UnFollowUsers(generics.GenericAPIView):
    queryset = CustomUser.objects.all()