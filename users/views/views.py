from django.contrib.messages import success
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers.token_obtain import MyTokenObtainPairSerializer
from users.serializers.user import UserSerializer
import uuid

from users.services import send_confirm_register_mail


class MyTokenObtainPairAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])  # Хэширование пароля
        user.key = uuid.uuid4()
        user.save()
        verify_email_url = reverse('users:verify_email', args=[user.key])

        send_confirm_register_mail(self, user, verify_email_url)

        return Response({success}, status.HTTP_201_CREATED)
        # email = serializer.validated_data.get('email')
        # password = serializer.validated_data.get('password')
        #
        # user = User.objects.create_user(
        #     email=email,
        #     password=password,
        # )
        #
        # serializer.save(email=user.email, password=user.password)


def verify_email(request, key):
    user = User.objects.get(key=key)

    if not user.is_active:
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
