from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from escuela.views import PersonaListar, PersonaCrear, PersonaEditar, PersonaBorrar, EscuelaListar, EscuelaCrear, VisitaListarA, VisitaListarB,VisitaCrear

urlpatterns = [
#    url(r'^$', index, name='index'),
    url(r'^listar_persona/', login_required(PersonaListar.as_view()), name='listar_persona'),
    url(r'^crear_persona/', login_required(PersonaCrear.as_view()), name='crear_persona'),

    url(r'^editar_persona/(?P<pk>\d+)/$', login_required(PersonaEditar.as_view()), name='editar_persona'),
    url(r'^borrar_persona/(?P<pk>\d+)/$', login_required(PersonaBorrar.as_view()), name='borrar_persona'),

    url(r'^listar_escuela/', login_required(EscuelaListar.as_view()), name='listar_escuela'),
    url(r'^crear_escuela/', login_required(EscuelaCrear.as_view()), name='crear_escuela'),
    url(r'^listar_visitaa/', login_required(VisitaListarA.as_view()), name='listar_visita'),
    url(r'^listar_visitab/', login_required(VisitaListarB.as_view()), name='listar_visita'),
    url(r'^crear_visita/', login_required(VisitaCrear.as_view()), name='crear_visita'),
]
