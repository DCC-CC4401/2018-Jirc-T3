from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.fichaArticulo, name='fichaArticulo'),
    url(r'^lista/$', views.lista, name='lista'),
    url(r'^reserva/$', views.reserva, name='reserva'),
    url(r'^editar/$', views.editar, name='editar'),
    url(r'^editarFoto/$', views.editarFoto, name='editarFoto'),
    url(r'^editarDes/$', views.editarDes, name='editarDes'),
    url(r'^editarRes/$', views.editarRes, name='editarRes'),
    url(r'^editarEst/$', views.editarEst, name='editarEst'),
    url(r'^aceptarnombre/$', views.aceptarNombre, name='aceptarNombre'),
    url(r'^cancelarnombre/$', views.cancelarNombre, name='cancelarNombre'),
    url(r'^aceptardes/$', views.aceptarDes, name='aceptarDes'),
    url(r'^aceptarest/$', views.aceptarEst, name='aceptarEst'),
    url(r'^aceptarfoto/$', views.aceptarFoto, name='aceptarFoto'),
    url(r'^aceptarres/$', views.aceptarRes, name='aceptarRes')
]
