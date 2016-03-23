from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^biografias/$', views.BiografiaView.as_view(), name='biografias'),
	url(r'^biografias/(?P<pk>[0-9]+)/$', views.BiografiaDetailView.as_view(), name='biografia'),
	url(r'^quienesSomos/$', views.quienesSomos, name='quienesSomos'),
	url(r'^objetivos/$', views.objetivos, name='objetivos'),
	url(r'^contacto/$', views.contacto, name='contacto'),
	url(r'^efemerides/$', views.efemerides, name='efemerides'),
	url(r'^benefactores/$', views.benefactores, name='benefactores'),
]