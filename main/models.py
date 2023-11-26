from django.db import models
from users.models import User
from constants import NULLABLE


class Habit(models.Model):
    """Модель привычки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             **NULLABLE, related_name='habit')
    place = models.CharField(max_length=50, verbose_name='место')
    time_to_start = models.TimeField(verbose_name='время начала')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_positive = models.BooleanField(default=False,
                                      verbose_name='признак приятной привычки')
    merge = models.ForeignKey('self', on_delete=models.SET_NULL,
                              **NULLABLE, related_name='habit',
                              verbose_name='связанная привычка')
    frequency = models.IntegerField(default=1, verbose_name='периодичность')
    reward = models.CharField(
        max_length=100, **NULLABLE, verbose_name='вознаграждение')
    time_to_complete = models.TimeField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False,
                                    verbose_name='признак публичности')

    def __str__(self):
        return (f'Я буду {self.action} в {self.time_to_start}. '
                f'Место - {self.place}')
