from django.contrib import admin

# Register your models here.
from trade.models import OrderInfo
 
class OrderInfoAdmin(admin.ModelAdmin):
    list_display=['ord_id','price','service_charge','freight','status','payment','user','address']

admin.site.register(OrderInfo,OrderInfoAdmin)