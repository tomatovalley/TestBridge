
from django.conf.urls import url
from TestBridgeApp import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
     url(r'^contact$', login_required(views.contact), name='contact'),
     url(r'^home$', login_required(views.home), name='home'),
     url(r'^', views.start, name='start'),



]