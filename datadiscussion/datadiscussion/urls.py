from django.conf.urls import include, url
from django.contrib import admin
import dataportal

urlpatterns = [
    # Examples:
    # url(r'^$', 'datadiscussion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dataportal/', include('dataportal.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', dataportal.views.index, name='index'),
    url(r'^view', dataportal.views.view_data, name='view_data'),
    url(r'^submit', dataportal.views.submit_data, name='submit_data'),
    url(r'^register', dataportal.views.register, name='register'),
    url(r'^about', dataportal.views.about, name='about'),
]
