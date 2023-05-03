# Generated by Django 4.2 on 2023-04-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='Logo'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='mfa',
            field=models.BooleanField(default=False, verbose_name='MFA'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='mfa_code',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Código MFA'),
        ),
    ]
