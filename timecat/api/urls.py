from django.urls import include, path

from rest_framework import routers

from apps.users.views import UsersViewSet
from apps.schedules.views import SchedulesViewSet
from apps.notes.views import NotesViewSet
from apps.habits.views import HabitsViewSet

router = routers.DefaultRouter()
# 若存在自定义get_queryset方法的视图集，则该视图集在注册时需设置base_name
router.register(r'users', UsersViewSet)
router.register(r'schedules', SchedulesViewSet, base_name='schedules')
router.register(r'notes', NotesViewSet, base_name='notes')
router.register(r'habits', HabitsViewSet, base_name='habits')

urlpatterns = [
  path('', include(router.urls)),
  path('rest-auth/', include('rest_auth.urls')),
  path('rest-auth/registration/', include('rest_auth.registration.urls')),
]