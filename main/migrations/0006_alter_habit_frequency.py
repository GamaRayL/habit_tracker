# Generated by Django 4.2.7 on 2023-11-24 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_habit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='frequency',
            field=models.CharField(choices=[(1, 'Каждый день'), (2, 'Каждые 2 дня'), (3, 'Каждые 3 дня'), (4, 'Каждые 4 дня'), (5, 'Каждые 5 дня'), (6, 'Каждые 6 дня'), (7, 'Каждую неделю')], default=1, help_text='Периодичность выполнения привычки для напоминания в днях', max_length=1, verbose_name='периодичность'),
        ),
    ]