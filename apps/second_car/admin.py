from django.contrib import admin

# Register your models here.
from second_car.models import CarStyle ,Brande,CarDetail,ImageDetail,IndexBanner

class CarDetailAdmin(admin.ModelAdmin):
    list_display=['car_model','color','car_age','gearbox','mileage','displacement','emission_standard','fuel_type','license_plate_location','drive','country','status','caruser','stype','brand']


admin.site.register(CarStyle)
admin.site.register(Brande)
admin.site.register(ImageDetail)
admin.site.register(CarDetail,CarDetailAdmin)
admin.site.register(IndexBanner)