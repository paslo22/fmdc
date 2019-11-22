from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^biografias/(?P<filtro>[\w ]+/)?$', views.BiografiaView.as_view(), name='biografias'),
    url(r'^biografia/(?P<pk>[0-9]+)/$', views.BiografiaDetailView.as_view(), name='biografia'),
    url(r'^consejoAdm/$', views.consejoAdm, name='consejoAdm'),
    url(r'^consejoCon/$', views.consejoCon, name='consejoCon'),
    url(r'^miembros/$', views.miembros, name='miembros'),
    url(r'^objetivos/$', views.objetivos, name='objetivos'),
    url(r'^material/$', views.material, name='material'),
    url(r'^partituras/(?P<path>[\w\d/ ]+/)?$', views.PartiturasCView.as_view(), name='partiturasC'),
    url(r'^letras/(?P<path>[\w\d/ ]+/)?$', views.LetrasCView.as_view(), name='letrasC'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^actividades/(?P<filtro>[\w ]+/)?$', views.ActividadView.as_view(), name='actividades'),
    url(r'^actividad/(?P<pk>[0-9]+)/$', views.ActividadDetailView.as_view(), name='actividad'),
    url(r'^efemerides/$', views.efemerides, name='efemerides'),
    url(r'^benefactores/$', views.benefactores, name='benefactores'),
    url(r'^discotecas/(?P<filtro>[\w ]+/)?$', views.DiscotecaView.as_view(), name='discotecas'),
    url(r'^discoteca/(?P<pk>[0-9]+)/$', views.DiscotecaDetailView.as_view(), name='discoteca'),
    url(r'^galerias/$', views.GaleriaView.as_view(), name='galerias'),
    url(r'^galeria/Fotos Chamameceros/(?P<path>[\w\d/ ]+/)?$', views.GaleriaCView.as_view(), name='galeriasC'),
    url(r'^galeria/(?P<path>[\w\d/ ]+/)?$', views.GaleriaDetailView.as_view(), name='galeria'),
    url(r'^videos/(?P<path>[\w\d/ ]+)?/?$', views.VideoView.as_view(), name='videos'),
    url(r'^busqueda/(?P<filtro>.+)?/$', views.BusquedaView.as_view(), name='busqueda'),
    url(r'^imagenesLaterales/$', views.imgLaterales, name='imagenesLaterales'),
    url(r'^tinymce/', include('tinymce.urls')),
]
