from rest_framework import viewsets, serializers
from apps.users.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'avatar']
