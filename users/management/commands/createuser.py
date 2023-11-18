from django.core.management import BaseCommand

from constants import MEMBER
from users.models import User


class Command(BaseCommand):
    """Команда для создания пользователя"""
    def handle(self, *args, **options):
        try:
            email = input('Почта: ')
            password = input('Пароль: ')
            user = User.objects.create_user(
                email=email,
                password=password,
            )
            user.save()

            self.stdout.write(self.style.SUCCESS(f'Пользователь {email} успешно создан!'))
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("\nПрограмма была прервана пользователем (Ctrl + C)"))