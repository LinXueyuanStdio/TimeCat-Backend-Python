from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer
  permission_classes = (IsAuthenticated,)