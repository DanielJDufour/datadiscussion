from django.contrib import admin
from dataportal.models import SiteInfo, Dataset, Twitter, Facebook, GIS, UserProfile

admin.site.register(SiteInfo)
admin.site.register(UserProfile)
admin.site.register(Dataset)
admin.site.register(Twitter)
admin.site.register(Facebook)
admin.site.register(GIS)

