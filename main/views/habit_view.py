from main.models import Habit
from main.serializers.habit_create_serializer import HabitCreateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView

from main.serializers.habit_list_serializer import HabitListSerializer


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitCurrentUserListAPIView(ListAPIView):
    serializer_class = HabitListSerializer
    queryset = Habit.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class HabitPublicListAPIView(ListAPIView):
    pass

