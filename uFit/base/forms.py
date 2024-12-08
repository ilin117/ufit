from django.forms import ModelForm
from .models import Post, Profile
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']        