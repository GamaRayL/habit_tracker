from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from constants import EXPECTED_CREATE_DATA
from main.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
            email='admin@test.com',
        )
        self.user.set_password('admin')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = {
            'place': 'дом',
            'time_to_start': '12:00',
            'action': 'делать курсовую',
            'frequency': 2,
            'reward': 'сон',
            'time_to_complete': '00:02',
        }

    def test_create_habit(self):
        """Тестирование создания привычки."""

        response = self.client.post('/habits/create/', data=self.habit)
        self.assertEqual(response.json(), EXPECTED_CREATE_DATA)
        self.assertTrue(Habit.objects.all().exists())

# class LessonTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = User.objects.create(
#             email='admin@test.com',
#             role='admin',
#             is_superuser=True,
#             is_staff=True,
#             is_active=True
#         )
#         self.user.set_password('admin')
#         self.user.save()
#         self.client.force_authenticate(user=self.user)
#
#         self.lesson = Lesson.objects.create(
#             name="New lesson",
#             description="New lesson description",
#             video_url="https://www.youtube.com/watch?v=nLRL_NcnK-4"
#         )
#
#     def test_create_lesson(self):
#         """ Тестирование создания урока """
#         data = {
#             "name": "New lesson",
#             "description": "New lesson description",
#             "video_url": "https://www.youtube.com/watch?v=nLRL_NcnK-4"
#         }
#
#         response = self.client.post('/lessons/create/', data=data)
#
#         self.assertEqual(response.json(), EXPECTED_CREATE_DATA)
#
#         self.assertTrue(Lesson.objects.all().exists())
#
#     def test_list_lesson(self):
#         """ Тестирование получения списка уроков """
#
#         response = self.client.get('/lessons/')
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#
#         self.assertEqual(
#             response.json(),
#             {
#                 "count": 1,
#                 "next": None,
#                 "previous": None,
#                 "results": [
#                     EXPECTED_DATA
#                 ]
#             }
#         )
