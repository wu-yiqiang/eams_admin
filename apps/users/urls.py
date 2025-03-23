from tokenize import Token

from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from apps.users.views import LoginView, RegisterView,UserView

app_name = 'users'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('<int:pk>', UserView.as_view({'get': 'retrieve'})),

]
