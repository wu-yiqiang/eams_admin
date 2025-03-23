from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.core.serializers import serialize
from django.db.models import Q
from rest_framework import serializers
from apps.users.models import Users

class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Users.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
        except :
            raise serializers.ValidationError({'msg': '未找到用户'})
        if user.check_password(password):
            return user
        else:
            raise serializers.ValidationError({"msg": '密码错误'})