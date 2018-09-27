from django.db import models

from apps.users.models import CustomUser


class NoteBook(models.Model):
    """
    Model: 笔记本
    """
    user = models.ForeignKey(CustomUser, verbose_name='用户', blank=True, null=True, on_delete=models.CASCADE)
    
    title = models.CharField('标题', max_length=100, blank=True, default='新笔记')
    content = models.TextField('内容', blank=True, default='')

    created_datetime = models.DateTimeField('创建时间', auto_now_add=True)
    update_datetime = models.DateTimeField('修改时间', auto_now=True)
    
    is_archived = models.BooleanField('是否归档', default=False)
    cover = models.TextField('封面', blank=True, default='')

    class Meta:
        db_table = "NoteBook"
        ordering = ('update_datetime', )
        verbose_name = '笔记本'
        verbose_name_plural = verbose_name


class Note(models.Model):
    """
    Model: 笔记
    """
    render_choices = (
        (0,'不渲染'),
        (1,'Markdown 渲染')
    )
    user = models.ForeignKey(CustomUser, verbose_name='用户', blank=True, null=True, on_delete=models.CASCADE)
    notebook = models.ForeignKey(NoteBook, verbose_name='笔记本', blank=True, null=True, on_delete=models.CASCADE)
    
    title = models.CharField('标题', max_length=100, blank=True, default='新笔记')
    content = models.TextField('内容', blank=True, default='')

    created_datetime = models.DateTimeField('创建时间', auto_now_add=True)
    update_datetime = models.DateTimeField('修改时间', auto_now=True)
    
    is_archived = models.BooleanField('是否归档', default=False)
    is_rawtext = models.BooleanField('是否纯文本', default=False)
    render_type = models.IntegerField('渲染类型', choices=render_choices, default=1)

    class Meta:
        db_table = "Notes"
        ordering = ('update_datetime', )
        verbose_name = '笔记'
        verbose_name_plural = verbose_name

