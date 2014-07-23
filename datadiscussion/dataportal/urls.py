from django.conf.urls import url




from dataportal import views

from django.contrib.auth.views import login, logout


from django.conf.urls import patterns, include, url
from dataportal.views import *


from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('view', views.view, name='view'),
    url('submit', views.submit, name='submit'),
    url('register', CreateView.as_view(
            template_name='dataportal/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),
    url('test', views.test, name='test'),
]
