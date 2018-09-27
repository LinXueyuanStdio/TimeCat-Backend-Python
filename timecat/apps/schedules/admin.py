from django.contrib import admin

import xadmin

from apps.schedules.models import Task, Plan, SubPlan

admin.site.register([Task, Plan, SubPlan])

@xadmin.sites.register(Task)
class TaskAdmin(object):
    list_display = ("id", "user", "title")
    list_display_links = ("user", "title")
    model_icon = 'fa fa-calendar'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()


@xadmin.sites.register(Plan)
class PlanAdmin(object):
    list_display = ("id", "user", "title")
    list_display_links = ("user", "title")
    model_icon = 'fa fa-calendar'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()


@xadmin.sites.register(SubPlan)
class SubPlanAdmin(object):
    list_display = ("id", "user", "title")
    list_display_links = ("user", "title")
    model_icon = 'fa fa-calendar'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

