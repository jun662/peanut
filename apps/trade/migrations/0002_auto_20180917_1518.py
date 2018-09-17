# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('second_car', '0002_auto_20180917_1518'),
        ('user', '0001_initial'),
        ('trade', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='address',
            field=models.ForeignKey(verbose_name='收货地址', to='user.UserAddress'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(verbose_name='所属用户', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordercar',
            name='car_id',
            field=models.ForeignKey(verbose_name='车辆编号', to='second_car.CarDetail'),
        ),
        migrations.AddField(
            model_name='ordercar',
            name='order',
            field=models.ForeignKey(verbose_name='订单车辆', to='trade.OrderInfo'),
        ),
    ]
