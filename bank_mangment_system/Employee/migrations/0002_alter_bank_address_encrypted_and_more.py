# Generated by Django 5.0.3 on 2024-03-23 22:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='address_encrypted',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_name_encrypted',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bank',
            name='branch_encrypted',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bank',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banks_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bank',
            name='established_date_encrypted',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banks_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
