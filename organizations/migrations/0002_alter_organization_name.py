# Generated by Django 3.2.4 on 2021-06-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Название'),
        ),
    ]
