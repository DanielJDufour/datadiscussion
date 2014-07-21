from django.contrib import admin
from dataportal.models import Dataset, Twitter, Facebook, GIS

admin.site.register(Dataset)
admin.site.register(Twitter, Facebook, GIS)
