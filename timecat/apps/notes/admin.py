from django.contrib import admin

import xadmin

from apps.notes.models import Note, NoteBook

admin.site.register([Note, NoteBook])

@xadmin.sites.register(Note)
class NoteAdmin(object):
    list_display = ("id", "user", "title")
    list_display_links = ("user", "title")
    model_icon = 'fa fa-book'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()


@xadmin.sites.register(NoteBook)
class NoteBookAdmin(object):
    list_display = ("id", "user", "title")
    list_display_links = ("user", "title")
    model_icon = 'fa fa-book'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()
