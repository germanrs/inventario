from django.conf.urls import url, include

from escuela.views import PersonaListar, PersonaCrear, EscuelaListar, EscuelaCrear

urlpatterns = [
#    url(r'^$', index, name='index'),
    url(r'^listar_persona/', PersonaListar.as_view(), name='persona_listar'),
    url(r'^crear_persona/', PersonaCrear.as_view(), name='persona_crear'),
    url(r'^listar_escuela/', EscuelaListar.as_view(), name='escuela_listar'),
    url(r'^crear_escuela/', EscuelaCrear.as_view(), name='escuela_crear'),
]