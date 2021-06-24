from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Введите пароль',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
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


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self, *args, **kwargs):
        cleaned_data = super(UserLoginForm, self).clean()

        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise ValidationError(_('Пользователь с такими данными не существует!'))
            if not self.user.is_active:
                raise ValidationError(_('Данный аккаунт не активен'))
        return cleaned_data

    def get_user(self):
        return self.user
