# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180914_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'verbose_name': '用户地址', 'verbose_name_plural': '用户地址'},
        ),
    ]
