from django.contrib.admin import ModelAdmin

from admins.admin.shop_staff import shop_admin
from .models import *


class PostAdmin(ModelAdmin):
    """

    """

class CategoryAdmin(ModelAdmin):
    """

    """

shop_admin.register(Category, ModelAdmin)
shop_admin.register(Post, ModelAdmin)


