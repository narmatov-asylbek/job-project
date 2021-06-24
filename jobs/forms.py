from django import forms
from django.forms import ValidationError
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('creator', 'is_expired', 'is_approved')

    def clean(self):
        cleaned_data = super(JobForm, self).clean()
        telegram = cleaned_data.get('telegram')
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')
        if not telegram and not email and not phone:
            raise ValidationError('Укажите контактные данные для отклика')
        return cleaned_data

    def clean_city(self):
        job_type = self.cleaned_data.get('type')
        city = self.cleaned_data.get('city')
        if job_type != 'remote' and city is None:
            raise ValidationError('Укажите город')
        return city

    def clean_salary_max(self):
        min_salary = self.cleaned_data.get('salary_min')
        max_salary = self.cleaned_data.get('salary_max')

        if (min_salary and not max_salary) or (max_salary and not min_salary):
            raise ValidationError('Укажите максимальную и минимальную зарплату')
        if int(min_salary) > int(max_salary):
            raise ValidationError('Максимальная зарплата не может быть меньше минимальной')
        return max_salary

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 100:
            raise ValidationError('Описание должно содержать минимум 100 символов')
        return description
