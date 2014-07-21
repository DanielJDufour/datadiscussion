from django.conf.urls import url

from dataportal import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.view, name='view'),
    url(r'^$', views.submit, name='submit'),
]
