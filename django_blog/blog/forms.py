from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget 
from django.forms import widgets


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Provide a valid email address.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Ensure 'tags' is included in the fields

    # Use TagWidget to render the tags field
    tags = forms.CharField(widget=TagWidget())


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']