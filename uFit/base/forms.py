from django.forms import ModelForm
from .models import Post, Profile
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }