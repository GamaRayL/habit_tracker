import datetime
from rest_framework.serializers import ValidationError


class TimeToCompleteValidator:
    """Валидатор времени выполнения"""
    def __init__(self, time_field):
        self.time_field = time_field

    def __call__(self, value):
        time = value.get(self.time_field)

        if time > datetime.time(minute=2):
            raise ValidationError('Время выполнения должно быть не больше 120 секунд!')