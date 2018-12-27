from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='devices'),
    url(r'^list/', views.list, name='list'),
    url(r'^create/',views.CreateDevices.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.EditDevices.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteDevices.as_view(),name='delete'),
    url(r'^query/(?P<pk>\d+)/$',views.query,name='query'),
]
