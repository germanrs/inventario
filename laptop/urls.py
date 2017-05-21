from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from laptop.views import index, LaptopListar, LaptopCrear, IncidenteListar, IncidenteCrear

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^listar/', login_required(LaptopListar.as_view()), name='listar_laptop'),
    url(r'^crear/', login_required(LaptopCrear.as_view()), name='crear_laptop'),
    url(r'^listar_incidente/', login_required(IncidenteListar.as_view()), name='listar_incidente'),
    url(r'^crear_incidente/', login_required(IncidenteCrear.as_view()), name='crear_incidente'),
]