from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^list', login_required(views.list), name='list'),
    url(r'^create', login_required(views.CreateDevices.as_view()),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.EditDevices.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteDevices.as_view(),name='delete'),
    url(r'^query/(?P<pk>\d+)/$',views.query,name='query'),
    
    url(r'^devices/$',views.DeviceApiCQ.as_view(),name='devicesCQ'),
    url(r'^devices/(?P<pk>\d+)/$',views.DeviceApiRUD.as_view(),name='devicesRUD'),
]
