from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    nickname = forms.CharField(
        label='닉네임',
        help_text='닉네임은 중복될 수 없습니다',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label='비밀번호',
        help_text=password_validation.password_validators_help_text_html(),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'nickname', 'email']


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['nickname', 'email']

        widgets = {
            'nickname': forms.TextInput(attrs={
                'class': 'col form-control',
                'style': 'margin-right: 1rem; margin-left: 1rem;'
            }),
            'email': forms.TextInput(attrs={
                'class': 'col form-control',
                'style': 'margin-right: 1rem; margin-left: 1rem;'
            }),
        }
        