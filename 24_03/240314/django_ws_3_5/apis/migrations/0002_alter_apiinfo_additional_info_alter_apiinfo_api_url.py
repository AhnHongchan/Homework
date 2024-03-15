# Generated by Django 4.2.11 on 2024-03-14 08:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinfo',
            name='additional_info',
            field=models.JSONField(blank=True, default='None', null=True),
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='api_url',
            field=models.URLField(validators=[django.core.validators.MinLengthValidator(limit_value=15), django.core.validators.MaxLengthValidator(limit_value=60)]),
        ),
    ]
