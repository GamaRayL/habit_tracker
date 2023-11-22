from rest_framework.serializers import ModelSerializer

from main.models import Habit
from main.validators.habit_validator import HabitValidator
from main.validators.time_to_complete_validator import TimeToCompleteValidator


class HabitSerializer(ModelSerializer):
    """Сериализатор привычки"""

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            HabitValidator(reward_field='reward', merge_field='merge', is_positive_field='is_positive'),
            TimeToCompleteValidator(time_field='time_to_complete')
        ]
