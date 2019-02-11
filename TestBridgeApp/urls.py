
from django.conf.urls import url
from TestBridgeApp import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
     url(r'^contact/$', login_required(views.contact), name='contact'),
     url(r'^home/$', login_required(views.home), name='home'),
     url(r'^pricing/$', views.pricing, name='pricing'),
     url(r'^resources/$', views.resources, name='resources'),
     url(r'^solutions/$', views.testingSolutions, name='solutions'),
     url(r'^testing/$', views.testing, name='testing'),
     url(r'^projectsCustomers/$', views.projectsCustomers, name='customers'),
     url(r'^project/(?P<pk>\d+)$', views.query, name='query'),
     url(r'^project/save/(?P<pk>\d+)/$', views.saveProject, name='save'),
     url(r'^home/delete/(?P<pk>\d+)/$', views.deleteProject, name='delete'),
     url(r'^$', views.start, name='start'),
]
