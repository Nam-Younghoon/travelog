from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # tag = forms.CharField(required=False, label='태그')
    class Meta:
        model = Post
        fields = ['title', 'body', 'thumbnail_image', 'category']

