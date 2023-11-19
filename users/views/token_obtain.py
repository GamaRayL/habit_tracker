from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers.token_obtain import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# class MyTokenRefreshView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer