from rest_framework import serializers
from apps.notes.models import Note

class NotesSerializer(serializers.ModelSerializer):
    is_rawtext = serializers.BooleanField(default=True)

    class Meta:
        model = Note
        fields = ('user', 'created_datetime', 'update_datetime',
            # 'subplan',
            'title', 'content',
            'is_rawtext',
        )
        read_only_fields = ('user', 'created_datetime')