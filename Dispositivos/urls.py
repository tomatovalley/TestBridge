from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='dispositivos'),
    url(r'^lista/', views.lista, name='lista'),
    url(r'^alta/',views.AltaDispositivo.as_view(),name='alta'),
    url(r'^modificar/(?P<pk>\d+)/$',views.modificarDispositivo.as_view(),name='modificacion'),
    url(r'^eliminar/(?P<pk>\d+)/$',views.eliminarDispositivo.as_view(),name='eliminar'),
    url(r'^consultar/(?P<pk>\d+)/$',views.consulta,name='consulta'),
]
