from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.fichaArticulo, name='fichaArticulo'),
    url(r'^reserva/$', views.reserva, name='reserva'),
    url(r'^editar/$', views.editar, name='editar'),
    url(r'^aceptarnombre/$', views.aceptarNombre, name='aceptarNombre')
]
