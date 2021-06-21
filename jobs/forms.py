from django import forms

from .models import Job


class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('creator', 'is_expired', 'is_approved')