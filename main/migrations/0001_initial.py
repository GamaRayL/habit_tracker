# Generated by Django 4.2.7 on 2023-11-18 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(help_text='Место, в котором необходимо выполнять привычку', max_length=50, verbose_name='место')),
                ('time_to_start', models.TimeField(help_text='Время, когда необходимо выполнять привычку', verbose_name='время начала')),
                ('action', models.CharField(help_text='Действие, которое представляет из себя привычка', max_length=100, verbose_name='действие')),
                ('is_positive', models.BooleanField(default=False, help_text='Привычка, которую можно привязать к выполнению полезной привычки', verbose_name='признак приятной привычки')),
                ('frequency', models.CharField(choices=[('daily', 'день'), ('weekly', 'неделя'), ('monthly', 'месяц')], default='день', help_text='Периодичность выполнения привычки для напоминания в днях', max_length=10, verbose_name='периодичность')),
                ('reward', models.CharField(help_text='Чем пользователь должен себя вознаградить после выполнения', max_length=100, verbose_name='вознаграждение')),
                ('time_to_complete', models.TimeField(help_text='Время, которое предположительно потратит пользователь на выполнение привычки', verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('merge', models.ForeignKey(blank=True, help_text='Привычка, которая связана с другой привычкой (важно указывать для полезных привычек, но не для приятных)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='habit', to='main.habit', verbose_name='связанная привычка')),
            ],
        ),
    ]
