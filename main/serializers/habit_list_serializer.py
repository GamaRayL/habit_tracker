from main.models import Habit
from rest_framework.serializers import ModelSerializer


class HabitListSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
