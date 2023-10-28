from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'thumbnail_image', 'category']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': '제목을 입력하세요...',
                'class': 'form-control'
            }),
            'thumbnail_image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            },),
        }


    


