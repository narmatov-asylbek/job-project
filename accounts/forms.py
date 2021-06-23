from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Введите пароль',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Первый пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {
            'email': None,
            'password1': None
        }
        error_messages = {
            'password_mismatch': 'Пароли не совпадают'
        }

