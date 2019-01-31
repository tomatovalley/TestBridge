from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/', views.list, name='list'),
    url(r'^create/',views.CreateTest.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.EditTest.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteTest.as_view(),name='delete'),
    url(r'^read/(?P<pk>\d+)/$',views.query,name='query'),
]
