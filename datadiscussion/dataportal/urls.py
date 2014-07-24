from dataportal import views
from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('view', views.view, name='view'),
    url('submit', views.submit, name='submit'),
    url('register', views.register, name='register'),
    url('^accounts/', include('django.contrib.auth.urls')),
    url('test', views.test, name='test'),
]
