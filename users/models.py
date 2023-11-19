from django.db import models
from django.apps import apps
from constants import USER_ROLES, MEMBER, ADMIN, NULLABLE
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Менеджер под создание пользователей"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Поле "email" должно быть заполнено!')
        email = self.normalize_email(email)
        global_user_model = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        email = global_user_model.normalize_username(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("role", MEMBER)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", ADMIN)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Модель пользователя"""
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    is_active = models.BooleanField(default=True, verbose_name='активен')
    key = models.CharField(max_length=100, **NULLABLE, verbose_name='ключ')
    role = models.CharField(max_length=20,
                            choices=USER_ROLES.items(), default=MEMBER,
                            verbose_name='роль')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
