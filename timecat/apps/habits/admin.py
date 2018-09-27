from django.contrib import admin

import xadmin

from apps.habits.models import Habit, Streak, Repetition, Score, CheckMark

admin.site.register([Habit, Streak, Repetition, Score, CheckMark])

@xadmin.sites.register(Habit)
class HabitAdmin(object):
    list_display = ("id", "user", "title", "created_datetime", "is_archived")
    list_display_links = ("user", "title")
    model_icon = 'fa fa-clock-o'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

@xadmin.sites.register(Streak)
class StreakAdmin(object):
    list_display = ("id", "habit", "start", "end", "length")
    list_display_links = ("habit",)
    model_icon = 'fa fa-clock-o'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

@xadmin.sites.register(Repetition)
class RepetitionAdmin(object):
    list_display = ("id", "habit", "timestamp")
    list_display_links = ("habit",)
    model_icon = 'fa fa-clock-o'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

@xadmin.sites.register(Score)
class ScoreAdmin(object):
    list_display = ("id", "habit", "timestamp", "score")
    list_display_links = ("habit",)
    model_icon = 'fa fa-clock-o'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

@xadmin.sites.register(CheckMark)
class CheckMarkAdmin(object):
    list_display = ("id", "habit", "timestamp", "value")
    list_display_links = ("habit",)
    model_icon = 'fa fa-clock-o'
    # inlines = [profileInline,]

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()
