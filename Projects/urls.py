from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^list', login_required(views.list), name='list'),
    url(r'^create', login_required(views.CreateProject.as_view()),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.EditProject.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteProject.as_view(),name='delete'),
    url(r'^read/(?P<pk>\d+)/$',views.query,name='query'),
    
    url(r'^functionalities/(?P<project_id>\d+)/$', views.functionalities, name='functionalities'),
    
    url(r'^projects/$',views.ProjectApiCQ.as_view(),name='projectCQ'),
    url(r'^projects/(?P<pk>\d+)/$',views.ProjectApiRUD.as_view(),name='projectRUD'),

]
