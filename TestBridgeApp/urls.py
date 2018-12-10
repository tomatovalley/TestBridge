
from django.conf.urls import url
from TestBridgeApp import views


urlpatterns = [
     url(r'^contact$', views.contact, name='contact'),
     url(r'^', views.home, name='home'),
]