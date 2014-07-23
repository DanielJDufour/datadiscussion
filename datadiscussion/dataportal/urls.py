from django.conf.urls import url

from dataportal import views

from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('view', views.view, name='view'),
    url('submit', views.submit, name='submit'),
    url('register', views.register, name='register'),
]
