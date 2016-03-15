from django.conf.urls import patterns, url
from appdelta.views import *

urlpatterns = patterns('',
    url(r'^index', Viewindex.as_view(), name='index'),
    url(r'^agregarclientes', Viewagregar.as_view(), name='agregarclientes'),
    url(r'^admin', Viewadmin.as_view(), name='admin'),
    url(r'^login', Viewlogin.as_view(), name='login'),
    url(r'^cerrarseccion', Viewcerrar.as_view(), name='cerrarseccion'),
    url(r'^inicio', Viewinicio.as_view(), name='inicio'),
    url(r'^informacion', Viewinformacion.as_view(), name='informacion'),
    url(r'^(?P<pk>\d+)/cambiarpassword/$', Vieweditar.as_view(), name="cambiarpassword"),    
    #url(r'^(?P<pk>\d+)/login/$', Viewlogin.as_view(), name="login"),
    url(r'^(?P<pk>\d+)/editarclientes/$', Vieweditar.as_view(), name="editarclientes"),
    url(r'^(?P<pk>\d+)/abono/$', Viewabono.as_view(), name="abono"),
    url(r'^(?P<pk>\d+)/verabonos/$', Viewmirar.as_view(), name="verabonos"),
    url(r'^(?P<pk>\d+)/admincliente/$', Viewadcliente.as_view(), name='admincliente'),
)