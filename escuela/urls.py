from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from escuela.views import (
    PersonaListar, 
    PersonaCrear, 
    PersonaEditar, 
    PersonaBorrar, 
    EscuelaListar, 
    EscuelaCrear, 
    VisitaCrear, 
    VisitaListar, 
    VisitaEditar, 
    VisitaBorrar,
    VisitaVer
    )
from escuela.views import (
    ChartData, IncidentesData1, IncidentesData2, IncidentesData3, Reporte1, Reporte2, 
    Reporte3, Reporte4, 
    Reporte5)
from donante.views import DonanteListar, DonanteCrear, DonanteEditar, DonanteBorrar

urlpatterns = [
#    url(r'^$', index, name='index'),
    url(r'^listar_persona/', login_required(PersonaListar.as_view()), name='listar_persona'),
    url(r'^crear_persona/', login_required(PersonaCrear.as_view()), name='crear_persona'),    
    url(r'^editar_persona/(?P<pk>\d+)/$', login_required(PersonaEditar.as_view()), name='editar_persona'),
    url(r'^borrar_persona/(?P<pk>\d+)/$', login_required(PersonaBorrar.as_view()), name='borrar_persona'),

    url(r'^listar_escuela/', login_required(EscuelaListar.as_view()), name='listar_escuela'),
    url(r'^crear_escuela/', login_required(EscuelaCrear.as_view()), name='crear_escuela'),

	url(r'^listar_donante/', login_required(DonanteListar.as_view()), name='listar_donante'),
	url(r'^crear_donante/', login_required(DonanteCrear.as_view()), name='crear_donante'),
    url(r'^editar_donante/(?P<pk>\d+)/$', login_required(DonanteEditar.as_view()), name='editar_donante'),
    url(r'^borrar_donante/(?P<pk>\d+)/$', login_required(DonanteBorrar.as_view()), name='borrar_donante'),

    url(r'^crear_visita/', login_required(VisitaCrear.as_view()), name='crear_visita'),
    url(r'^listar_visita/', login_required(VisitaListar.as_view()), name='listar_visita'),
    
    url(r'^ver_visita/(?P<pk>\d+)/$', login_required(VisitaVer.as_view()), name='ver_visita'),

    url(r'^editar_visita/(?P<pk>\d+)/$', login_required(VisitaEditar.as_view()), name='editar_visita'),
    url(r'^borrar_visita/(?P<pk>\d+)/$', login_required(VisitaBorrar.as_view()), name='borrar_visita'),

    url(r'^api/chart/data/', ChartData.as_view()),
    url(r'^api/chart/incidentes_data1/', IncidentesData1.as_view()),
    url(r'^api/chart/incidentes_data2/', IncidentesData2.as_view()),
    url(r'^api/chart/incidentes_data3/', IncidentesData3.as_view()),
    url(r'^reporte1', Reporte1.as_view(), name='reporte1'),
    url(r'^reporte2', Reporte2.as_view(), name='reporte2'),
    url(r'^reporte3', Reporte3.as_view(), name='reporte3'),
    url(r'^reporte4', Reporte4.as_view(), name='reporte4'),
    url(r'^reporte5', Reporte5.as_view(), name='reporte5'),    
]
