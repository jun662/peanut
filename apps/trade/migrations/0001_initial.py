# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('commet', models.CharField(verbose_name='评论', max_length=100)),
            ],
            options={
                'verbose_name': '车辆信息',
                'verbose_name_plural': '车辆信息',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('ord_id', models.CharField(verbose_name='订单号', primary_key=True, max_length=15, serialize=False)),
                ('price', models.DecimalField(verbose_name='交易价格', max_digits=10, decimal_places=2)),
                ('service_charge', models.DecimalField(verbose_name='手续费', max_digits=10, decimal_places=2)),
                ('freight', models.DecimalField(verbose_name='运费', max_digits=10, decimal_places=2)),
                ('status', models.IntegerField(verbose_name='订单状态', default=0, choices=[(0, '未支付'), (1, '已支付'), (2, '未运输'), (3, '运输中'), (4, '交易成功'), (5, '交易失败')])),
                ('payment', models.IntegerField(verbose_name='支付方式', default=0, choices=[(0, '线下支付'), (1, '线上支付'), (2, '找人代付'), (3, '贷款支付')])),
                ('online_payment', models.IntegerField(verbose_name='付款方式', default=2, choices=[(0, '银联支付'), (1, '微信支付'), (2, '支付宝')])),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
    ]
