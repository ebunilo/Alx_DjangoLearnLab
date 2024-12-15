from django.urls import path, include
from notifications import views
from rest_framework import routers

notification_router = routers.DefaultRouter()
notification_router.register(r'', views.NotificationView, basename='notifications')



urlpatterns = [
    path('notifications/', include(notification_router.urls)),
]