from django.db import models
from db.basemodel import BaseModel
# Create your models here.

class OrderInfo(BaseModel):
    order_status=((0,'未支付'),(1,'已支付'),(2,'未运输'),(3,'运输中'),(4,'交易成功'),(5,'交易失败'))
    
    ord_id=models.CharField(max_length=15, verbose_name ='订单号',primary_key=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='交易价格')
    service_charge=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='手续费')
    freight=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='运费')
    status =models.IntegerField(default=0,choices=order_status,verbose_name="订单状态")

    payment_status=((0,'线下支付'),(1,'线上支付'),(2,'找人代付'),(3,'贷款支付'))
    ONLINE_PAY=((0,'银联支付'),(1,'微信支付'),(2,'支付宝'))

    payment=models.IntegerField(choices=payment_status,default=0,verbose_name="支付方式")
    user = models.ForeignKey('user.PeanutInfo',verbose_name='所属用户')
    address = models.ForeignKey('user.UserAddress',verbose_name='收货地址')
    online_payment=models.IntegerField(choices=ONLINE_PAY,default=2,verbose_name='付款方式')
    class Meta:
        verbose_name='订单信息'
        verbose_name_plural=verbose_name


class OrderCar(BaseModel):
    order=models.ForeignKey('OrderInfo',verbose_name='订单车辆')
    car_id=models.ForeignKey('second_car.CarDetail',verbose_name='车辆编号')
    commet=models.CharField(max_length=100,verbose_name='评论')
    class Meta:
        verbose_name='车辆信息'
        verbose_name_plural=verbose_name

