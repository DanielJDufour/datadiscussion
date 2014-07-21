from django.conf.urls import url

from dataportal import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$/view', views.view, name='view'),
    url(r'^$/submit', views.submit, name='submit'),
]
