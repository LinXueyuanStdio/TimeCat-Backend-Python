from django.contrib import admin

import xadmin

from apps.notes.models import Note

admin.site.register([Note])

@xadmin.sites.register(Note)
class NoteAdmin(object):
    list_display = ("id", "user", "title")
    list_display_links = ("user", "title")
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()