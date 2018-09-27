from django.db import models


# 引入Enum类型
from enum import Enum
from enumfields import EnumIntegerField

from apps.users.models import CustomUser


class CheckMarkLabel(Enum):
    UNCHECK = 0
    CHECKED_IMPLICITY = 1
    CHECKED_EXPLICITY = 2

class Habit(models.Model):
    """
    Model: 习惯
    """
    user = models.ForeignKey(CustomUser, verbose_name='用户', blank=True, null=True, on_delete=models.CASCADE)
    
    title = models.CharField('标题', max_length=100, blank=True, default='新习惯')
    content = models.TextField('内容', blank=True, default='')

    created_datetime = models.DateTimeField('创建时间', auto_now_add=True)
    update_datetime = models.DateTimeField('修改时间', auto_now=True)
    
    is_archived = models.BooleanField('是否归档', default=False)
    
    freqNum = models.IntegerField('渲染类型', default=1)
    freqDen = models.IntegerField('渲染类型', default=1)

    reminderDay = models.IntegerField('提醒天数', default=0)
    reminderHour = models.IntegerField('提醒小时数', default=0)
    reminderMin = models.IntegerField('提醒分钟数', default=0)

    color = models.CharField('颜色', blank=True, max_length=9, default=r"#ffffffff") # "#ff123456"

    class Meta:
        db_table = "Habit"
        ordering = ('update_datetime', )


class Streak(models.Model):
    """
    Model: 习惯
    """
    habit = models.ForeignKey(Habit, verbose_name='习惯', blank=True, null=True, on_delete=models.CASCADE)
    
    start = models.IntegerField('开始', default=0)
    end = models.IntegerField('结束', default=0)
    length = models.IntegerField('持续时长', default=0)

    class Meta:
        db_table = "Streak"
        ordering = ('id', )


class Repetition(models.Model):
    """
    Model: 习惯
    """
    habit = models.ForeignKey(Habit, verbose_name='习惯', blank=True, null=True, on_delete=models.CASCADE)
    
    timestamp = models.IntegerField('时间戳', default=0)

    class Meta:
        db_table = "Repetition"
        ordering = ('timestamp', )


class CheckMark(models.Model):
    """
    Model: 习惯标记是否完成
    """
    habit = models.ForeignKey(Habit, verbose_name='习惯', blank=True, null=True, on_delete=models.CASCADE)
    
    timestamp = models.IntegerField('时间戳', default=0)
    value = EnumIntegerField(CheckMarkLabel, verbose_name='标记状态', default=CheckMarkLabel.UNCHECK)

    class Meta:
        db_table = "CheckMark"
        ordering = ('timestamp', )



class Score(models.Model):
    """
    Model: 习惯分数
    """
    habit = models.ForeignKey(Habit, verbose_name='习惯', blank=True, null=True, on_delete=models.CASCADE)
    
    timestamp = models.IntegerField('时间戳', default=0)
    score = models.IntegerField('分数', default=0)

    class Meta:
        db_table = "Score"
        ordering = ('timestamp', )
