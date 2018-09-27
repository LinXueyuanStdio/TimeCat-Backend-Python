from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.habits.models import Habit, Streak, Repetition, Score, CheckMark
from apps.habits.serializers import HabitsSerializer, StreaksSerializer, RepetitionsSerializer, ScoresSerializer, CheckMarksSerializer

class HabitsViewSet(viewsets.ModelViewSet):
    serializer_class = HabitsSerializer
    permission_classes = (IsAuthenticated, )

    # 当前用户自定义类型或默认类型
    def get_queryset(self):
        return Habit.objects.filter(
            Q(user=self.request.user))

    # 创建时默认设置用户关联关系
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # 更新时再次更新用户关联关系
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class StreaksViewSet(viewsets.ModelViewSet):
    serializer_class = StreaksSerializer
    permission_classes = (IsAuthenticated, )


class RepetitionsViewSet(viewsets.ModelViewSet):
    serializer_class = RepetitionsSerializer
    permission_classes = (IsAuthenticated, )


class ScoresViewSet(viewsets.ModelViewSet):
    serializer_class = ScoresSerializer
    permission_classes = (IsAuthenticated, )


class CheckMarksViewSet(viewsets.ModelViewSet):
    serializer_class = CheckMarksSerializer
    permission_classes = (IsAuthenticated, )

