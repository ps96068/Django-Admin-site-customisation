from django.apps import apps
from django.contrib.admin import apps as adminApps, sites


class MyAdminConfig(adminApps.AdminConfig):
    default_site = 'admins.admin.admin.MyAdminSite'

    def ready(self, *args, **kwargs):
        super().ready(*args, **kwargs)
        sites.site.name = 'admin'

        site = sites.site  # chaged with multiply admin sites
        site._registry = {}  # remove old registrations

        all_apps_file = apps.get_app_configs()
        for config in all_apps_file:
            admins = getattr(config.module, 'admin', None)

            for model in config.get_models():  # excluded auto_created and swapped
                model_admin = getattr(admins, f'{model.__name__}Admin', None)
                if model_admin and not site.is_registered(model):
                    site.register(model, model_admin)


