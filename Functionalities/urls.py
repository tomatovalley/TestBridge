from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/', views.list, name='list'),
    url(r'^create/',views.CreateFunctionality.as_view(),name='create'),
    url(r'^query/(?P<pk>\d+)/$',views.query,name='query'),
    url(r'^update/(?P<pk>\d+)/$',views.EditFunctionality.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteFunctionality.as_view(),name='delete'),
]
