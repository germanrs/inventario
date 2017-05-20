from django.conf.urls import url, include

from escuela.views import PersonaListar, PersonaCrear, EscuelaListar, EscuelaCrear, VisitaListar, VisitaCrear

urlpatterns = [
#    url(r'^$', index, name='index'),
    url(r'^listar_persona/', PersonaListar.as_view(), name='listar_persona'),
    url(r'^crear_persona/', PersonaCrear.as_view(), name='crear_persona'),
    url(r'^listar_escuela/', EscuelaListar.as_view(), name='listar_escuela'),
    url(r'^crear_escuela/', EscuelaCrear.as_view(), name='crear_escuela'),
    url(r'^listar_visita/', VisitaListar.as_view(), name='listar_visita'),
    url(r'^crear_visita/', VisitaCrear.as_view(), name='crear_visita'),

]