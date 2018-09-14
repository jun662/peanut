# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brande',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='车辆品牌', max_length=10)),
            ],
            options={
                'verbose_name': '车辆品牌',
                'verbose_name_plural': '车辆品牌',
            },
        ),
        migrations.CreateModel(
            name='CarDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('car_model', models.CharField(verbose_name='车型', max_length=5)),
                ('color', models.CharField(verbose_name='车的颜色', max_length=5)),
                ('car_age', models.CharField(verbose_name='车龄', max_length=10)),
                ('gearbox', models.CharField(verbose_name='变速箱', max_length=10)),
                ('mileage', models.DecimalField(verbose_name='里程数', max_digits=10, decimal_places=2)),
                ('displacement', models.CharField(verbose_name='排量', max_length=10)),
                ('emission_standard', models.CharField(verbose_name='排放标准', max_length=10)),
                ('fuel_type', models.CharField(verbose_name='燃油类型', max_length=10)),
                ('license_plate_location', models.CharField(verbose_name='车辆所在地', max_length=20)),
                ('drive', models.CharField(verbose_name='驱动类型', max_length=10)),
                ('country', models.CharField(verbose_name='国别', max_length=10)),
                ('status', models.IntegerField(verbose_name='车辆出售状态', default=1, choices=[(0, '下线'), (1, '上线')])),
                ('brand', models.ForeignKey(verbose_name='所属品牌', to='second_car.Brande')),
                ('caruser', models.ForeignKey(verbose_name='所属用户', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '车辆细节',
                'verbose_name_plural': '车辆细节',
            },
        ),
        migrations.CreateModel(
            name='CarStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('car_name', models.CharField(verbose_name='车辆类型', max_length=10)),
                ('image', models.ImageField(verbose_name='车型代表图片', upload_to='type')),
            ],
            options={
                'verbose_name': '车辆类型',
                'verbose_name_plural': '车辆类型',
            },
        ),
        migrations.CreateModel(
            name='ImageDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('path', models.ImageField(verbose_name='车辆细节图', upload_to='/detail_img')),
                ('index', models.IntegerField(verbose_name='顺序')),
                ('car_detail', models.ForeignKey(verbose_name='车辆细节图', to='second_car.CarDetail')),
            ],
            options={
                'verbose_name': '车辆细节图',
                'verbose_name_plural': '车辆细节图',
            },
        ),
        migrations.CreateModel(
            name='IndexBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('path', models.ImageField(verbose_name='图片', upload_to='/banner')),
                ('index', models.IntegerField(verbose_name='顺序')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.AddField(
            model_name='cardetail',
            name='stype',
            field=models.ForeignKey(verbose_name='所属车型', to='second_car.CarStyle'),
        ),
    ]
