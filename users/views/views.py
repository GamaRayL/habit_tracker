from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers.token_obtain import MyTokenObtainPairSerializer
from users.serializers.user import UserSerializer


class MyTokenObtainPairAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])  # Хэширование пароля
        user.save()
        # email = serializer.validated_data.get('email')
        # password = serializer.validated_data.get('password')
        #
        # user = User.objects.create_user(
        #     email=email,
        #     password=password,
        # )
        #
        # serializer.save(email=user.email, password=user.password)