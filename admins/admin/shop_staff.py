from .admin import MyAdminSite
from django.utils.translation import gettext_lazy as _

class ShopAdminSite(MyAdminSite):
    permission = None
    site_header = _("Django shop admin")

shop_admin = ShopAdminSite(name='shop-admin')