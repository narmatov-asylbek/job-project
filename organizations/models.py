from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Organization(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organizations',
        verbose_name=_('Создатель')
    )
    logo = models.ImageField(
        upload_to='logos/%Y/%m/%d',
        blank=True,
        null=True,
        verbose_name=_('Логотип')
    )
    name = models.CharField(max_length=120, unique=True, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    website = models.URLField(null=True, blank=True, verbose_name=_('Веб-сайт'))

    class Meta:
        ordering = ['id', 'name']
        verbose_name = _('Организация')
        verbose_name_plural = _('Организации')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organizations:organization-detail', args=[self.id])

    def get_jobs_count(self):
        return self.jobs.filter(organization_id=self.id, is_approved=True).count()
