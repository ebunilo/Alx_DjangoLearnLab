from django.shortcuts import render
from notifications.serializers import NotificationSerializer
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from notifications.models import Notification
from rest_framework import permissions

# Create your views here.
class NotificationView(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=True)
    def likepost(self, request, pk=None):
        pass

    @action(methods=['post'], detail=True)
    def unlikepost(self, request, pk=None):
        pass