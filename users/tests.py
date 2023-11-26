from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from users.models import User


class UserAPITestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            'email': 'test@user.com',
            'password': 'test',
            'tg_chat_id': '1234'
        }

    def test_user_register(self) -> None:
        """Тестирование регистрации нового пользователя."""
        response = self.client.post('/users/register/', data=self.data)
        self.assertEqual(response.json(), {'message': 'Пользователь успешно создан'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verify_email(self) -> None:
        """Тестирование подтверждения почты новым пользователем."""
        self.client.post('/users/register/', data=self.data)

        user = User.objects.all().first()
        url = reverse('users:verify_email', args=[user.key])

        response_verify = self.client.post(url)
        self.assertEqual(response_verify.json(), {'message': 'Email successfully confirmed'})
        self.assertEqual(response_verify.status_code, status.HTTP_200_OK)

    def test_token_obtain_pair(self) -> None:
        """Тестирование получения токена пользователя."""
        self.client.post('/users/register/', data=self.data)

        user = User.objects.all().first()
        url = reverse('users:verify_email', args=[user.key])
        self.client.post(url)

        response = self.client.post('/users/token/', data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)