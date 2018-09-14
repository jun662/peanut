# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='add',
        ),
        migrations.AddField(
            model_name='useraddress',
            name='address',
            field=models.CharField(verbose_name='收货人地址', max_length=50, default=0),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='is_delete',
            field=models.IntegerField(verbose_name='是否删除', default=0),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='recv_name',
            field=models.CharField(verbose_name='收货人', max_length=10, default=0),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='recv_phone',
            field=models.IntegerField(verbose_name='联系方式', default=0),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='rervice_phone',
            field=models.IntegerField(verbose_name='客服电话', default=0),
        ),
    ]
