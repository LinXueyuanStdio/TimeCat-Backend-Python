from django.contrib import admin

import xadmin

from apps.schedules.models import Task

admin.site.register([Task])

@xadmin.sites.register(Task)
class TaskAdmin(object):
    list_display = ("id", "user", "title")
    list_display_links = ("user", "title")
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()