# Generated by Django 2.0.5 on 2018-09-27 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180913_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='color',
            field=models.CharField(blank=True, default='#ffffffff', max_length=9, verbose_name='颜色'),
        ),
    ]