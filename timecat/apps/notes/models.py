from django.db import models

from apps.users.models import CustomUser

class Note(models.Model):
    """
    Model: 笔记
    """
    user = models.ForeignKey(CustomUser, verbose_name='用户', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=100, blank=True, default='新笔记')
    content = models.TextField('内容', blank=True, default='')

    created_datetime = models.DateTimeField('创建时间', auto_now_add=True)
    update_datetime = models.DateTimeField('修改时间', auto_now=True)
    
    is_archived = models.BooleanField('是否归档', default=False)
    is_rawtext = models.BooleanField('是否纯文本', default=False)

    class Meta:
        db_table = "notes"
        ordering = ('update_datetime', )