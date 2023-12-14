# Generated by Django 4.2.7 on 2023-11-24 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_habit_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='frequency',
            field=models.IntegerField(default=1, help_text='Периодичность выполнения привычки для напоминания в днях', verbose_name='периодичность'),
        ),
    ]
