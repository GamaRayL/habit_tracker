# Generated by Django 4.2.7 on 2023-11-23 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_habit_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='frequency',
            field=models.CharField(choices=[('день', 'день'), ('неделя', 'неделя')], default='день', help_text='Периодичность выполнения привычки для напоминания в днях', max_length=10, verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(blank=True, help_text='Создатель привычки', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
