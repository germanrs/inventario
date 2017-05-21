from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from escuela.views import PersonaListar, PersonaCrear, EscuelaListar, EscuelaCrear, VisitaListar, VisitaCrear

urlpatterns = [
#    url(r'^$', index, name='index'),
    url(r'^listar_persona/', login_required(PersonaListar.as_view()), name='listar_persona'),
    url(r'^crear_persona/', login_required(PersonaCrear.as_view()), name='crear_persona'),
    url(r'^listar_escuela/', login_required(EscuelaListar.as_view()), name='listar_escuela'),
    url(r'^crear_escuela/', login_required(EscuelaCrear.as_view()), name='crear_escuela'),
    url(r'^listar_visita/', login_required(VisitaListar.as_view()), name='listar_visita'),
    url(r'^crear_visita/', login_required(VisitaCrear.as_view()), name='crear_visita'),

]