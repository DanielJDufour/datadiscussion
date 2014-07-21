from django.contrib import admin
from dataportal.models import Dataset
from dataportal.models import Twitter
from dataportal.models import Facebook
from dataportal.models import GIS


admin.site.register(Dataset)
admin.site.register(Twitter)
admin.site.register(Facebook)
admin.site.register(GIS)
