from django.urls import path
from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import MyTokenObtainPairAPIView, UserRegisterAPIView, \
    verify_email

app_name = UsersConfig.name

urlpatterns = [
    path('token/', MyTokenObtainPairAPIView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('verify_email/<uuid:key>/', verify_email, name='verify_email'),
]
