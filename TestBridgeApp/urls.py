
from django.conf.urls import url
from TestBridgeApp import views


urlpatterns = [
     url(r'^profile/(?P<username>\w{1,50})/$',views.user_edit, name='profile'),
     url(r'^contact$', views.contact, name='contact'),
     url(r'^', views.home, name='home'),

]