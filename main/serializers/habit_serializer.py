from rest_framework.relations import SlugRelatedField

from main.models import Habit
from rest_framework.serializers import ModelSerializer


class HabitSerializer(ModelSerializer):
    """Сериализатор для модели Habit."""
    class Meta:
        model = Habit
        fields = ('id', 'place', 'time_to_start', 'action', 'is_positive',
                  'time_to_complete', 'is_public', 'user')


class HabitListSerializer(ModelSerializer):
    """Сериализатор привычки."""
    merge = HabitSerializer()

    class Meta:
        model = Habit
        fields = ('id', 'place', 'time_to_start', 'action', 'is_positive',
                  'frequency', 'reward', 'time_to_complete', 'is_public', 'user', 'merge')
