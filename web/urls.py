from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^biografias/(?P<filtro>[a-zA-Z ]+/)?$', views.BiografiaView.as_view(), name='biografias'),
	url(r'^biografia/(?P<pk>[0-9]+)/$', views.BiografiaDetailView.as_view(), name='biografia'),
	url(r'^quienesSomos/$', views.quienesSomos, name='quienesSomos'),
	url(r'^objetivos/$', views.objetivos, name='objetivos'),
	url(r'^contacto/$', views.contacto, name='contacto'),
	url(r'^efemerides/$', views.efemerides, name='efemerides'),
	url(r'^benefactores/$', views.benefactores, name='benefactores'),
	url(r'^discotecas/(?P<filtro>[a-zA-Z ]+/)?$', views.DiscotecaView.as_view(), name='discotecas'),
	url(r'^discoteca/(?P<pk>[0-9]+)/$', views.DiscotecaDetailView.as_view(), name='discoteca'),
]