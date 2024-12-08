from typing import Any

from django import forms
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

from blog.models import Post, Comment, Tag
from blog.forms import UserRegisterForm, PostCreationForm, CommentForm, SearchForm, ProfileManagementForm

User = get_user_model
class RegisterView(CreateView):
    """Ä view to create new user instances"""

    template_name = 'register.html'
    form_class = UserRegisterForm
    model = User
    success_url = reverse_lazy('profile')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class ProfileManagementView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    """A view to manage user profiles requires users to LogIn"""
    template_name = 'profile_management.html'
    model = User
    form_class = ProfileManagementForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileManagementForm(instance=user)
        context['user'] = self.request.user
        return context
    
    def get_success_url(self) -> str:
        return reverse ('profile')
    
    def form_valid(self, form: forms.BaseModelForm) -> HttpResponse:

        user_bio = form.cleaned_data.get('bio')
        user_photo = form.cleaned_data.get('profile_picture')
        user = self.request.user
        
        profile = user.profile  
        profile.bio = user_bio
        profile.profile_picture = user_photo
        profile.save()

        user.save()
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user == self.get_object()

class HomeView(TemplateView):
    template_name ='home.html'

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'post_create.html'
    model = Post
    form_class = PostCreationForm

    def form_valid(self, form):
        post_author = self.request.user
        form.instance.author = post_author
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.has_perm('blog.add_post')
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'post_update.html'
    model = Post
    fields = ['title', 'content']

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = reverse_lazy('posts')

    def is_owner(self):
        post = self.get_object()
        return self.request.user == post.author

    def test_func(self):
        return self.is_owner()
    
class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_create_post'] = self.request.user.has_perm('blog.add_post')
        return context

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comment'] = self.get_object().post_comments.all()
        return context
    
class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'post_detail.html'
    model = Comment

    def form_valid(self, form):
        """Handle the valid form submission, save the comment and redirect"""
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden('<h1>Sorry You Cannot Create a Comment You have to be a user</h1>')
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post  # Attach the comment to the post
        form.instance.author = self.request.user# Attach the comment to the user
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('post-detail', kwargs={'pk':self.kwargs['pk']})

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object().post

class CommentListView(ListView):
    """ A view to list all comments associated with a Post"""
    template_name = 'blog/comment_list.html'
    model = Comment
    context_object_name = 'comment_list'

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ A view for authenticated and users of comments to update their comments"""
    model = Comment
    template_name = 'blog/comment_update.html'
    fields = ['content']

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().author

    def get_success_url(self) -> str:
        return reverse ('post-detail', kwargs={'pk':self.get_object().post.pk})

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object().post
        return context
    
class CommentDeleteView(DeleteView):
    """ A view for users to delete their comments"""
    model = Comment
    context_object_name = 'comment'
    success_url = reverse_lazy('comment-list')
    # permission_required = ['blog.delete_post']
    template_name = 'blog/comment_delete.html'

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().author
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object().post
        return context   

class PostDetailCommentView(View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentCreateView.as_view()
        return view(request, *args, **kwargs)




def search_view(request):
    queryset = Post.objects.all()
    form = SearchForm()

    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['to_search']
            searched_items = queryset.filter(Q(title__icontains=query)|Q(content__icontains=query))
        else:
            form = SearchForm()
    context = {
        'post_list': searched_items,
        'search_form': form,
    }
    return render(request, 'search.html', context=context)

def tag_view(request, tag_name):
    tag = get_object_or_404(klass=Tag, name__iexact=tag_name)
    post_by_tag = Post.objects.filter(Q(tags__name__icontains=tag.name))

    context = {
        'posts':post_by_tag,
        'tag_name':tag_name
    }

    return render(request, 'tags.html', context=context)

@login_required
@user_passes_test
def dummy(request):
    if request.method == "POST":
        form = RegisterForm(instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()

    return render(request, 'post_list.html', {'dummy':dummy})

def commentdummy(request, pk):
    return render(request, 'comment_create.html', {'dummy':dummy})

class PostByTagListView(ListView):
    model = Post
    template_name = 'tags.html'