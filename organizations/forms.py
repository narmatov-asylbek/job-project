from django import forms
from django.forms import ValidationError

from .models import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['logo', 'name', 'description', 'website']