from django.urls import path
from main.apps import MainConfig
from main.views.habit_view import HabitCreateAPIView

app_name = MainConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='create_habit'),
]