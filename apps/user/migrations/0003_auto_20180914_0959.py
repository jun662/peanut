# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180914_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='peanutinfo',
            name='first_name',
            field=models.CharField(verbose_name='first name', max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='peanutinfo',
            name='last_name',
            field=models.CharField(verbose_name='last name', max_length=30, blank=True),
        ),
    ]
