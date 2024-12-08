from taggit.forms import TagWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from blog.models import Post, Comment, Tag


User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ProfileManagementForm(UserChangeForm):
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        exclude = ['password']


class PostCreationForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=50,
        required=False,
        widget=TagWidget())
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            "content": forms.Textarea(attrs={"cols": 80, "rows": 20}),
        }

    def save(self, commit = True):
        instance = super().save(commit)
        post_instance = instance.id
        tag = self.cleaned_data['tags']
        if tag:
            Tag.objects.create(name=tag, posts=post_instance)
        if commit:
            instance.save()
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class SearchForm(forms.Form):
    to_search = forms.CharField(
        max_length=150,
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Search...',

            }
        ))
