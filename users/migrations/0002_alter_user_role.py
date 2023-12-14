# Generated by Django 4.2.7 on 2023-11-18 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'администратор'), ('member', 'участник')], default='участник', max_length=20, verbose_name='роль'),
        ),
    ]
