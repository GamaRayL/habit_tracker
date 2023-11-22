from main.models import Habit
from main.serializers.habit_serializer import HabitSerializer
from main.serializers.habit_create_serializer import HabitCreateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView


class HabitCurrentUserListAPIView(ListAPIView):
    """Список привычек текущего пользователя."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class HabitPublicListAPIView(ListAPIView):
    """Список публичных привычек."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        return self.queryset.filter(is_public=True)


class HabitCreateAPIView(CreateAPIView):
    """Добавление новой привычки."""
    serializer_class = HabitCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateAPIView(UpdateAPIView):
    """Редактирование привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
