from django.conf.urls import url, include

from laptop.views import index, LaptopListar, LaptopCrear

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^listar/', LaptopListar.as_view(), name='laptop_listar'),
    url(r'^crear/', LaptopCrear.as_view(), name='laptop_crear'),
]