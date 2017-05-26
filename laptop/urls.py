from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from laptop.views import index, LaptopListar, LaptopCrear, LaptopEditar, LaptopBorrar, \
						 IncidenteListar, IncidenteCrear, IncidenteEditar, IncidenteBorrar

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^listar/', login_required(LaptopListar.as_view()), name='listar_laptop'),
    url(r'^crear/', login_required(LaptopCrear.as_view()), name='crear_laptop'),
    
    url(r'^editar_laptop/(?P<pk>\d+)/$', login_required(LaptopEditar.as_view()), name='editar_laptop'),
    url(r'^borrar_laptop/(?P<pk>\d+)/$', login_required(LaptopBorrar.as_view()), name='borrar_laptop'),

    url(r'^listar_incidente/', login_required(IncidenteListar.as_view()), name='listar_incidente'),
    url(r'^crear_incidente/', login_required(IncidenteCrear.as_view()), name='crear_incidente'),

    url(r'^editar_incidente/(?P<pk>\d+)/$', login_required(IncidenteEditar.as_view()), name='editar_incidente'),
    url(r'^borrar_incidente/(?P<pk>\d+)/$', login_required(IncidenteBorrar.as_view()), name='borrar_incidente'),
]