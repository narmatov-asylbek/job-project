from django.db import models

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from organizations.models import Organization


class Job(models.Model):
    TYPE_CHOICES = (
        ('office', _('Работа в офисе')),
        ('project', _('Разовая работа над проектом')),
        ('remote', _('Удаленная работа')),
        ('internship', _('Стажировка'))
    )

    SALARY_CHOICES = (
        ('monthly', _('Месячный оклад')),
        ('hourly', _('Почасовая оплата')),
        ('fixed', _('Фиксированная'))
    )

    CURRENCY_CHOICES = (
        ('KGS', 'KGS'),
        ('USD', 'USD'),
        ('EURO', 'EURO'),
        ('RUB', 'RUB')
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='jobs',
        verbose_name=_('Вакансия')
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='jobs',
        verbose_name=_('Организация')
    )
    job_position = models.CharField(max_length=100, verbose_name=_('Должность'))
    description = models.TextField(verbose_name=_('Описание работы'))
    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Telegram'))
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('E-mail'))
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Номер телефона'))
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name=_('Тип работы'))
    salary = models.CharField(max_length=30, choices=SALARY_CHOICES, verbose_name=_('Оклад'))
    salary_min = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Минимальная зарплата'))
    salary_max = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Максимальная зарплата'))
    currency = models.CharField(max_length=4,
                                choices=CURRENCY_CHOICES,
                                null=True,
                                blank=True,
                                verbose_name=_('Валюта'))
    city = models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            verbose_name=_('Город'))
    is_expired = models.BooleanField(blank=True, default=False, verbose_name=_('Актуальность'))
    is_approved = models.BooleanField(blank=True, default=False, verbose_name=_('Подтвердить'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', 'updated_at']
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')

    def __str__(self):
        return self.job_position
