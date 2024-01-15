from django.contrib.admin import AdminSite, sites, ModelAdmin
from django.utils.translation import gettext_lazy as _

class MyAdminSite(AdminSite):
    name = 'admin'
    permission = 'is_superuser'
    site_header = _("Django super admin")

    def get_app_list(self, request, app_label=None):
        return list(self._build_app_dict(request, app_label).values())

    def has_permission(self, request):
        return super().has_permission(request) and (
                    not getattr(self, 'permission', None) or request.user.has_perm(self.permission))


    def admin_view(self, view, cacheable=False):
        def wrapper(func):
            def wrapped(*args, **kwargs):
                instance = getattr(func, '__self__', None)
                if isinstance(instance, ModelAdmin):
                    new_instance = type(instance)(instance.model, instance.admin_site)
                    return func.__func__(new_instance, *args, **kwargs)
                return func(*args, **kwargs)

            return wrapped

        return super().admin_view(wrapper(view), cacheable=False)


default_admin = sites.site