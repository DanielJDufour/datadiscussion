from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'datadiscussion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dataportal/', include('dataportal.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
