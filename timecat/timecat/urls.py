"""timecat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="时光猫 API 文档",
      default_version='v1',
      description="时光猫 API 文档",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="linxy59@mail2.sysu.edu.cn"),
      license=openapi.License(name="Apache License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

import xadmin
xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

from apps.users.views import LoginView,RegisterView,LogoutView,ForgetPwdView,ActiveUserView,ResetView,ModifyPwdView,IndexView
from timecat.settings.local import MEDIA_ROOT

# api and admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# docs
urlpatterns += [
    re_path(r'^docs/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    re_path(r'^docs/swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    re_path(r'^docs/redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]

# users
urlpatterns += [
    path('', IndexView.as_view(),name='index'),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('captcha/',include('captcha.urls')),
]

# resource
urlpatterns += [
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),

    #静态文件
    # re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATICFILES_DIRS }),

    # 富文本相关url
    path('ueditor/',include('DjangoUeditor.urls' )),
]

# apps
urlpatterns += [
    # 课程机构app相关url配置
    path("org/", include('apps.organization.urls', namespace="org")),
    # 课程app相关url配置
    path("course/", include('apps.course.urls', namespace="course")),
    #个人信息
    path("users/", include('apps.users.urls', namespace="users")),
]

# 全局404页面配置
handler404 = 'apps.users.views.pag_not_found'
# 全局500页面配置
handler500 = 'apps.users.views.page_error'