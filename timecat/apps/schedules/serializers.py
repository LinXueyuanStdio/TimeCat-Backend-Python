from rest_framework import serializers
from apps.schedules.fields import EnumField
from apps.schedules.models import Label, Task

class TaskSerializer(serializers.ModelSerializer):
    label = EnumField(enum=Label)
    is_all_day = serializers.BooleanField(default=True)

    class Meta:
        model = Task
        fields = ('user', 'created_datetime', 'update_datetime',
            # 'subplan',
            'title', 'content', 'label',
            # 'tags',
            'is_finished', 'finished_datetime',
            'is_all_day', 'begin_datetime', 'end_datetime',
        )
        read_only_fields = ('user', 'created_datetime')