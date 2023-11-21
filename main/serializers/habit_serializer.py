from rest_framework.serializers import ModelSerializer

from main.models import Habit
from main.validators.habit_validator import HabitValidator


class HabitSerializer(ModelSerializer):
    """Сериализатор привычки"""

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            HabitValidator(reward_field='reward', merge_field='merge', is_positive='is_positive')
        ]
