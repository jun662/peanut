from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class PeanutInfo(AbstractUser):
    # user_name=models.CharField(max_length=20,verbose_name="账号")
    # password=models.CharField(max_length=20,verbose_name="密码")
    # gender=models.BooleanField()
    # phone=models.IntegerField(max_length=20,verbose_name="手机号")
    # regist_time=models.DateTimeField()
    # update_time=models.DateTimeField()
    is_delete=models.IntegerField(default=0)
   
    # def __str__(self):
    #     return self.user_name
class UserAddress(models.Model):
    user_id=models.ForeignKey('PeanutInfo')
    recv_name=models.CharField(max_length=10,default=0,null=False,verbose_name="收货人")
    recv_phone=models.IntegerField(default=0,null=False,verbose_name="联系方式")
    rervice_phone=models.IntegerField(default=0,null=False,verbose_name="客服电话")
    address=models.CharField(max_length=50,default=0,null=False,verbose_name="收货人地址")
    is_delete=models.IntegerField(default=0,verbose_name="是否删除")
    class Meta:
        verbose_name="用户地址"
        verbose_name_plural=verbose_name

    # def __str__(self):
    #     return self.user