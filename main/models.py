from django.db import models
from users.models import User
from constants import FREQUENCY, DAILY, NULLABLE


class Habit(models.Model):
    """Модель привычки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь',
                             help_text='Создатель привычки')
    place = models.CharField(max_length=50, verbose_name='место',
                             help_text='Место, в котором необходимо выполнять привычку')
    time_to_start = models.TimeField(verbose_name='время начала',
                                     help_text='Время, когда необходимо выполнять привычку')
    action = models.CharField(max_length=100, verbose_name='действие',
                              help_text='Действие, которое представляет из себя привычка')
    is_positive = models.BooleanField(default=False,
                                      verbose_name='признак приятной привычки',
                                      help_text='Привычка, которую можно привязать к выполнению полезной привычки')
    merge = models.ForeignKey('self', on_delete=models.SET_NULL,
                              **NULLABLE, related_name='habit',
                              verbose_name='связанная привычка',
                              help_text='Привычка, которая связана с другой привычкой (важно указывать для полезных '
                                        'привычек, но не для приятных)')
    frequency = models.CharField(max_length=10,
                                 choices=FREQUENCY.items(), default=DAILY,
                                 verbose_name='периодичность',
                                 help_text='Периодичность выполнения привычки для напоминания в днях')
    reward = models.CharField(max_length=100, verbose_name='вознаграждение',
                              help_text='Чем пользователь должен себя вознаградить после выполнения')
    time_to_complete = models.TimeField(verbose_name='время на выполнение',
                                        help_text='Время, которое предположительно потратит пользователь на '
                                                  'выполнение привычки')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time_to_start} в {self.place}'
