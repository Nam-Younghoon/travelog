from typing import Any
from django import http
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView, TemplateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:user_login')

class UserLogoutView(LogoutView):
    next_page = 'home:home'

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True
    next_page = 'blog:blog_list'

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

class UserChangePasswordView(PasswordChangeView):
    template_name = 'user/password_change_form.html'
    success_url = reverse_lazy("user:user_password_change_done")

    

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'user/password_change_done.html'

    def get(self, request, *args, **kwargs):
        request.session.flush()
        logout(request)
        return super().get(request, *args, **kwargs)
    
class UserProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'user/update.html'
    form_class = CustomUserChangeForm
    model = get_user_model()
    success_url = reverse_lazy('user:user_profile')

    def test_func(self) -> bool | None:
        return self.get_object() == self.request.user
    
class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'user/user_confirm_delete.html'
    model = get_user_model()
    success_url = reverse_lazy('home:home')

    def test_func(self) -> bool | None:
        return self.get_object() == self.request.user






user_register = UserRegisterView.as_view()
user_logout = UserLogoutView.as_view()
user_login = UserLoginView.as_view()
user_profile = UserProfileView.as_view()
user_delete = UserDeleteView.as_view()
user_change_password = UserChangePasswordView.as_view()
user_change_password_done = UserPasswordChangeDoneView.as_view()
user_update = UserProfileUpdateView.as_view()
