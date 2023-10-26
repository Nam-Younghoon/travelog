from django.shortcuts import render
from django.views.generic import TemplateView

home = TemplateView.as_view(
    template_name = 'home/home.html'
)
