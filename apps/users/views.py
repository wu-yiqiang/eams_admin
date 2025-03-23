import json
from tokenize import TokenError
from rest_framework import status, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import InvalidToken

from apps.users.serializers import UserSerializer
from service_error.user import USER_RERROR
from service_success.common import COMMON_SUCCESS
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.models import Users
from utils.validate import isStrongPassword, isEmail
from django.contrib.auth.backends import BaseBackend

class LoginView(TokenObtainPairView):
    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        result = serializer.validated_data
        return Response(result, status=status.HTTP_200_OK)



class RegisterView(APIView):
    def post(self,request, *args, **kwargs):
        email = request.data.get('username')
        password = request.data.get('password')
        if not all([email, password]):
            return Response(USER_RERROR.USER_AND_PASSWORD_IS_REQUIRED, status=status.HTTP_200_OK)
        if Users.objects.filter(email=email).exists():
            return Response(USER_RERROR.USER_IS_EXIST, status=status.HTTP_200_OK)
        if not isEmail(email):
            return Response(USER_RERROR.EMAIL_IS_ILLEGAL, status=status.HTTP_200_OK)
        if not isStrongPassword(password):
            return Response(USER_RERROR.PASSWORD_IS_WEAK, status=status.HTTP_200_OK)
        try:
            user = Users.objects.create_user(email=email, password=password, username=email)
            user.save()
        except:
            return Response(USER_RERROR.CREATE_USER_FAILED, status=status.HTTP_200_OK)
        return Response(COMMON_SUCCESS.OPEARTIN_SUCCESS, status=status.HTTP_200_OK)


class LogoutView(APIView):
    pass

class UserView(GenericViewSet,mixins.RetrieveModelMixin):
    queryset = Users.objects.all()
    serializer_class = UserSerializer