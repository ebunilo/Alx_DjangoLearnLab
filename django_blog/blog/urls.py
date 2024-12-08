from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.ProfileManagementView.as_view(), name='profile-manager'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('home/', views.HomeView.as_view(), name='home'),

    path('post/<int:pk>/', views.PostDetailCommentView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/', views.PostListView.as_view(), name='posts'),

    path('comment/', views.CommentListView.as_view(),name='comment-list'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(),name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(),name='comment-delete'),
    path('post/<int:pk>/comments/new/', views.commentdummy, name='comment-dummy'),

    path('tags/<tag_name>/', views.tag_view, name='post-tag'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post-tag_list'),
    path('search/', views.search_view, name='post-search'),
]