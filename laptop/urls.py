from django.conf.urls import url, include

from laptop.views import index, LaptopListar, LaptopCrear, IncidenteListar, IncidenteCrear

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^listar/', LaptopListar.as_view(), name='listar_laptop'),
    url(r'^crear/', LaptopCrear.as_view(), name='crear_laptop'),
    url(r'^listar_incidente/', IncidenteListar.as_view(), name='listar_incidente'),
    url(r'^crear_incidente/', IncidenteCrear.as_view(), name='crear_incidente'),
]