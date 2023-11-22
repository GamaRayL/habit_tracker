from rest_framework.exceptions import ValidationError

from constants import FREQUENCY


class FrequencyValidator:
    def __init__(self, frequency_field):
        self.frequency_field = frequency_field

    def call(self, value):
        frequency = value.get(self.frequency_field)

        if frequency not in FREQUENCY.values():
            raise ValidationError('Нельзя выполнять привычку реже 1 раза в неделю. Укажитье "день" или "неделя"!')