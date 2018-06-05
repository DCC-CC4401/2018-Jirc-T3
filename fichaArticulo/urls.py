import django.conf.urls

from . import views

urlpatterns = [
    django.conf.urls.url(r'^$', views.fichaArticulo, name='fichaArticulo')
]
