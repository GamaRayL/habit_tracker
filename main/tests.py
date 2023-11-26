from main.models import Habit
from users.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from constants import EXPECTED_CREATE_DATA, EXPECTED_DATA, EXPECTED_CURRENT_HABIT_LIST, EXPECTED_UPDATE_DATA


class HabitAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
            email='admin@test.com',
        )
        self.user.set_password('admin')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place='дом',
            time_to_start='12:00',
            action='делать курсовую',
            frequency=2,
            reward='сон',
            time_to_complete='00:02',
            is_public=True,
            user=self.user
        )

    def tearDown(self) -> None:
        # Очистка базы данных перед каждым тестом.
        User.objects.all().delete()
        Habit.objects.all().delete()

    def test_create_habit(self):
        """Тестирование создания привычки."""
        data = {
            'place': 'дом',
            'time_to_start': '12:00',
            'action': 'делать курсовую',
            'frequency': 2,
            'reward': 'сон',
            'time_to_complete': '00:02',
            'is_public': True
        }

        response = self.client.post('/habits/create/', data=data)
        self.assertEqual(response.json(), EXPECTED_CREATE_DATA)
        self.assertTrue(Habit.objects.all().exists())

    def test_public_habit_list(self):
        """Тестирование получения списка публичных привычек."""
        response = self.client.get('/habits/public/')
        self.assertEqual(response.json(), [EXPECTED_DATA])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_current_user_habit_list(self):
        """Тестирование получения списка привычек текущего пользователя."""
        response = self.client.get('/habits/')
        self.assertEqual(response.json(), EXPECTED_CURRENT_HABIT_LIST)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        """Тестирование редактирования привычки."""
        data = {
            'time_to_start': '14:00',
            'action': 'делать зарядку',
            'reward': 'сок',
            'time_to_complete': '00:01',
        }

        response = self.client.patch(f'/habits/update/{self.habit.id}/', data=data)
        self.assertEqual(response.json(), EXPECTED_UPDATE_DATA)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        """Тестирование удаления привычки."""
        response = self.client.delete(f'/habits/delete/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)