from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^svapp/simpleform', views.extract, name='extract'),
    url(r'^$', views.index, name='index')]

