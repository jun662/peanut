# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('second_car', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetail',
            name='caruser',
            field=models.ForeignKey(verbose_name='所属用户', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cardetail',
            name='stype',
            field=models.ForeignKey(verbose_name='所属车型', to='second_car.CarStyle'),
        ),
    ]
