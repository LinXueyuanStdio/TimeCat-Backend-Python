from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.notes.models import Note
from apps.notes.serializers import NotesSerializer

class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    permission_classes = (IsAuthenticated, )

    # 当前用户自定义类型或默认类型
    def get_queryset(self):
        return Note.objects.filter(
            Q(user=self.request.user))

    # 创建时默认设置用户关联关系
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # 更新时再次更新用户关联关系
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
