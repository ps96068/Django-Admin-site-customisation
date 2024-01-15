from django.contrib.admin import ModelAdmin

from admins.admin.shop_staff import shop_admin
from .models import *



class ShopAdmin(ModelAdmin):
   pass

class ImageAdmin(ModelAdmin):
    pass

class ProductAdmin(ModelAdmin):
    pass

shop_admin.register(Shop, ShopAdmin)
shop_admin.register(Image, ModelAdmin)
shop_admin.register(Product, ModelAdmin)