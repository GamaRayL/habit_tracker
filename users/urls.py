from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views.views import MyTokenObtainPairAPIView, UserRegisterAPIView


urlpatterns = [
    path('token/', MyTokenObtainPairAPIView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', UserRegisterAPIView.as_view(), name='register'),
]