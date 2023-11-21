from rest_framework.generics import CreateAPIView

from main.serializers.habit_serializer import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # serializer = self.get_serializer(obj, data=request.data)
        # habit = serializer.save(habit=self.request.habit)
        # habit.user = self.request.user
        # habit.save()


