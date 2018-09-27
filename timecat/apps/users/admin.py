from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.users.models import CustomUser


import xadmin
from xadmin import views

# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '时光猫后台管理界面'
    # 修改footer
    site_footer = '时光猫'
    # 收起菜单
    menu_style = 'accordion'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)

# xadmin.site.register(CustomUser, CustomUserAdmin)

from .models import EmailVerifyRecord, Banner

# xadmin中这里是继承object，不再是继承admin


class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
