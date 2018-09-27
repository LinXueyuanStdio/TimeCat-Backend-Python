from rest_framework import serializers
from apps.habits.fields import EnumField
from apps.habits.models import CheckMarkLabel, Habit, Streak, Repetition, Score, CheckMark

class HabitsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Habit
        fields = ('user', 'created_datetime', 'update_datetime',
            # 'subplan',
            'title', 'content',
        )
        read_only_fields = ('user', 'created_datetime')

class StreaksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Streak
        fields = ('habit', 'start', 'end', 'length'
        )

class RepetitionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Repetition
        fields = ('habit', 'timestamp')
        

class ScoresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Score
        fields = ('habit', 'timestamp')
        
class CheckMarksSerializer(serializers.ModelSerializer):
    value = EnumField(enum=CheckMarkLabel)
    class Meta:
        model = CheckMark
        fields = ('habit', 'timestamp', 'value')
