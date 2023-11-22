from main.models import Habit
from rest_framework.serializers import ModelSerializer


class HabitSerializer(ModelSerializer):
    """Сериализатор привычки."""
    class Meta:
        model = Habit
        fields = '__all__'
