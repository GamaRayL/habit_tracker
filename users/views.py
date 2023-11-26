import uuid
from users.models import User
from rest_framework import status
from django.http import JsonResponse
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.serializers.user import UserSerializer
from users.services import send_confirm_register_mail
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView, get_object_or_404
from users.serializers.token_obtain import MyTokenObtainPairSerializer


class MyTokenObtainPairAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegisterAPIView(CreateAPIView):
    """Регистрация пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Создание пользователя и передача в сервисный слой адреса для подтверждения почты пользователя."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        verify_email_url = reverse('users:verify_email', args=[user.key])
        absolute_verify_email_url = request.build_absolute_uri(verify_email_url)
        send_confirm_register_mail(user, absolute_verify_email_url)

        return Response({'message': 'Пользователь успешно создан'}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        """Сохранение пользователя в базе данных."""
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.key = uuid.uuid4()
        user.save()

        return user


def verify_email(request, key):
    """Подтверждение почты пользователя"""
    user = get_object_or_404(User, key=key)

    if not user.is_active:
        user.is_active = True
        user.save()
        return JsonResponse({'message': 'Email successfully confirmed'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'message': 'Email already confirmed'}, status=status.HTTP_400_BAD_REQUEST)
