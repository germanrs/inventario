from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from donante.views import DonanteListar, DonanteCrear, DonanteEditar, DonanteBorrar

urlpatterns = [
	url(r'^listar_donante/', login_required(DonanteListar.as_view()), name='listar_donante'),
	url(r'^crear_donante/', login_required(DonanteCrear.as_view()), name='crear_donante'),
	#url(r'^editar_donante/(?P<pk>\d+)/$', login_required(DonanteEditar.as_view()), name='editar_donante'),
    #url(r'^borrar_donante/(?P<pk>\d+)/$', login_required(DonanteBorrar.as_view()), name='borrar_donante'),
]