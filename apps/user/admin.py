from django.contrib import admin

# Register your models here.
from user.models import PeanutInfo, UserAddress

class PeanutInfoAdmin(admin.ModelAdmin):
    list_display=['id','password','last_login','is_superuser','username','email','is_staff','is_active','is_delete']

class UserAddressAdmin(admin.ModelAdmin):
    list_display=['id','recv_name','recv_phone','rervice_phone','is_delete','user_id_id','address']

admin.site.register(PeanutInfo,PeanutInfoAdmin)
admin.site.register(UserAddress,UserAddressAdmin)