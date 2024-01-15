from django.urls import path
from django.contrib.admin.sites import all_sites

urlpatterns = [
    path(f'{site.name}/', site.urls) for site in all_sites
]

