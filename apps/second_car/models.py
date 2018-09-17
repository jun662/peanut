from django.db import models

# Create your models here.
class CarStyle(models.Model):
    car_name=models.CharField(max_length=10,verbose_name="车辆类型")
    image=models.ImageField(upload_to='type',verbose_name="车型代表图片")
    class Meta:
        verbose_name='车辆类型'
        verbose_name_plural=verbose_name

class Brande(models.Model):
    name=models.CharField(max_length=10,verbose_name='车辆品牌')
    class Meta:
        verbose_name='车辆品牌'
        verbose_name_plural=verbose_name

class CarDetail(models.Model):
    car_model=models.CharField(max_length=5,verbose_name='车型')
    color=models.CharField(max_length=5,verbose_name='车的颜色')
    car_age=models.CharField(max_length=10,verbose_name='车龄')
    gearbox=models.CharField(max_length=10,verbose_name='变速箱')
    mileage=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='里程数')
    displacement=models.CharField(max_length=10,verbose_name='排量')
    emission_standard=models.CharField(max_length=10,verbose_name='排放标准')
    fuel_type=models.CharField(max_length=10,verbose_name='燃油类型')
    license_plate_location=models.CharField(max_length=20,verbose_name='车辆所在地')
    drive=models.CharField(max_length=10,verbose_name='驱动类型')
    country=models.CharField(max_length=10,verbose_name='国别')
    status_choice=((0,'下线'),(1,"上线"))
    car_price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='二手车价格')
    status=models.IntegerField(default=1,choices=status_choice,verbose_name='车辆出售状态')
    caruser=models.ForeignKey('user.PeanutInfo',verbose_name="所属用户")
    stype=models.ForeignKey('CarStyle',verbose_name='所属车型')
    brand=models.ForeignKey('Brande',verbose_name='所属品牌')

    class Meta:
        verbose_name='车辆细节'
        verbose_name_plural=verbose_name

class ImageDetail(models.Model):
    path=models.ImageField(upload_to='/detail_img',verbose_name="车辆细节图")
    index=models.IntegerField(verbose_name='顺序')
    car_detail=models.ForeignKey('CarDetail',verbose_name="车辆细节图")
    class Meta:
        verbose_name="车辆细节图"
        verbose_name_plural=verbose_name

class IndexBanner(models.Model):
    path=models.ImageField(upload_to="/banner",verbose_name='图片')
    index=models.IntegerField(verbose_name="顺序")
    
    class Meta:
        verbose_name="轮播图"
        verbose_name_plural=verbose_name