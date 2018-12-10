from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='proyectos'),
    url(r'^lista/', views.lista, name='lista'),
    url(r'^alta/',views.AltaProyecto.as_view(),name='alta'),
    url(r'^modificar/(?P<pk>\d+)/$',views.modificarProyecto.as_view(),name='modificacion'),
    url(r'^eliminar/(?P<pk>\d+)/$',views.eliminarProyecto.as_view(),name='eliminar'),
    url(r'^consultar/(?P<pk>\d+)/$',views.consulta,name='consulta'),
]
