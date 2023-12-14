from rest_framework.exceptions import ValidationError


class FrequencyValidator:
    def __init__(self, frequency_field):
        self.frequency_field = frequency_field

    def __call__(self, value):
        frequency = value.get(self.frequency_field)

        if frequency <= 1 or frequency >= 7:
            raise ValidationError(
                'Периодичность должна быть в диапазоне от 1 до 7 (дни)'
            )
