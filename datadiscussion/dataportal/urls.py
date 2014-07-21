from django.conf.urls import url

from dataportal import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
