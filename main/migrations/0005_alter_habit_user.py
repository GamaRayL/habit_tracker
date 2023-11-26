# Generated by Django 4.2.7 on 2023-11-23 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_habit_frequency_alter_habit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(blank=True, help_text='Создатель привычки', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]