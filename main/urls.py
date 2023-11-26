from django.urls import path
from main.apps import MainConfig
from main.views.habit_view import HabitCreateAPIView, HabitPublicListAPIView, \
    HabitCurrentUserListAPIView, HabitUpdateAPIView, HabitDeleteAPIView

app_name = MainConfig.name

urlpatterns = [
    path('', HabitCurrentUserListAPIView.as_view(),
         name='current_user_habits'),
    path('public/', HabitPublicListAPIView.as_view(),
         name='public_habits'),
    path('create/', HabitCreateAPIView.as_view(),
         name='create_habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(),
         name='update_habit'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(),
         name='delete_habit'),
]
