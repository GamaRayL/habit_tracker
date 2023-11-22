from django.http import request

from main.models import Habit
from rest_framework import status
from rest_framework.response import Response

from main.permissions.is_owner import IsOwner
from main.serializers.habit_serializer import HabitListSerializer
from main.serializers.habit_create_serializer import HabitCreateSerializer
from main.paginations.current_user_habits_pagination import CurrentUserHabitsPagination
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from main.services.send_msg_to_tg import send_msg_to_tg


class HabitCurrentUserListAPIView(ListAPIView):
    """Список привычек текущего пользователя (с пагинацией)."""
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer
    pagination_class = CurrentUserHabitsPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class HabitPublicListAPIView(ListAPIView):
    """Список публичных привычек."""
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_public=True)


class HabitCreateAPIView(CreateAPIView):
    """Добавление новой привычки."""
    serializer_class = HabitCreateSerializer
    bot_token = '6795892672:AAEuABnRXf7MIXPhUMXqSl2rtMOdhaq8Mfg'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateAPIView(UpdateAPIView):
    """Редактирование привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        send_msg_to_tg()


class HabitDeleteAPIView(DestroyAPIView):
    """Удаление привычки."""
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        habit = self.get_object()
        habit.delete()
        return Response({'message': 'Привычка удалена.'}, status=status.HTTP_204_NO_CONTENT)
