from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(ur'^biografias/(?P<filtro>[\w ]+/)?$', views.BiografiaView.as_view(), name='biografias'),
	url(r'^biografia/(?P<pk>[0-9]+)/$', views.BiografiaDetailView.as_view(), name='biografia'),
	url(r'^quienesSomos/$', views.quienesSomos, name='quienesSomos'),
	url(r'^objetivos/$', views.objetivos, name='objetivos'),
	url(r'^material/$', views.material, name='material'),
	url(r'^partituras/(?P<filtro>[\w]+/)$', views.partituras, name='partituras'),
	url(r'^cancionero/(?P<filtro>[\w]+/)$', views.cancionero, name='cancionero'),
	url(r'^contacto/$', views.contacto, name='contacto'),
	url(r'^construccion/$', views.construccion, name='construccion'),
	url(r'^efemerides/$', views.efemerides, name='efemerides'),
	url(r'^benefactores/$', views.benefactores, name='benefactores'),
	url(ur'^discotecas/(?P<filtro>[\w ]+/)?$', views.DiscotecaView.as_view(), name='discotecas'),
	url(r'^discoteca/(?P<pk>[0-9]+)/$', views.DiscotecaDetailView.as_view(), name='discoteca'),
	url(ur'^galerias/(?P<path>[\w\d ]+/)?$',views.GaleriaView.as_view(), name='galerias'),
	url(ur'^galeria/(?P<path>[\w\d/ ]+/)?$', views.GaleriaDetailView.as_view(), name='galeria'),
]
