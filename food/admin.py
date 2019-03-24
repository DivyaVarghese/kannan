from django.contrib import admin
from food.models import CustomerR,Foodlist,HotelReg,Cart,Offer,Order,Rate

# Register your models here.
admin.site.register(CustomerR)
admin.site.register(Cart)
admin.site.register(Foodlist)
admin.site.register(HotelReg)
admin.site.register(Order)
admin.site.register(Rate)
admin.site.register(Offer)