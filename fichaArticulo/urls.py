from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.fichaArticulo, name='fichaArticulo'),
    url(r'^reserva/$', views.reserva, name='reserva')
]
