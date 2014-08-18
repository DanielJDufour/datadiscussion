from django.contrib import admin
from dataportal.models import SiteInfo, Dataset, Theme, Twitter, Facebook, GIS, DatasetFormat, Location

admin.site.register(SiteInfo)
admin.site.register(Dataset)
admin.site.register(Twitter)
admin.site.register(Facebook)
admin.site.register(GIS)
admin.site.register(Theme)
admin.site.register(DatasetFormat)
admin.site.register(Location)
