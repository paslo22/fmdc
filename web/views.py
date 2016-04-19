# -*- coding: utf-8 -*- 
from django.shortcuts import render,redirect
from django.http import Http404
from django.views import generic
from datetime import datetime
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.serializers.json import DjangoJSONEncoder
from django.template import Context
from django.contrib.staticfiles.templatetags.staticfiles import static
from PIL import Image
import os, re, json
from .models import Biografia, Efemeride, Discoteca, EfemerideMes
from .forms import ContactForm
from django.conf import settings

def index(request):
	return render(request, 'web/index.html')

class GaleriaView(generic.ListView):
	template_name = 'web/galerias.html'

	def get_queryset(self):
		return {
			'images' : os.listdir(settings.MEDIA_ROOT+'/archive/Galeria/Fotos'),
			'videos' : os.listdir(settings.MEDIA_ROOT+'/archive/Galeria/Videos'),
		}

class GaleriaCView(generic.DetailView):
	template_name = 'web/galeriaWithLetters.html'

	def get_object(self):
		obj = {}
		img = []
		pat = re.compile(ur'(.+)\.(?:png|jpg|PNG|JPG)', re.UNICODE)
		try:
			path = self.kwargs['path']
		except:
			raise Http404("Galeria no existe")
		if path == None:
			path = ''
		path = unicode(path)
		for url in os.listdir((settings.MEDIA_ROOT + '/archive/Galeria/Fotos/Fotos Chamameseros/' + path).encode('utf-8')):
			try:
				url = unicode(url.decode('utf-8'))
				im=Image.open((settings.MEDIA_ROOT + 'archive/Galeria/Fotos/Fotos Chamameseros/' + path + url).encode('utf-8'))
				re.match(pat,url).group(1)
			except:
				continue
			img.append({'url':settings.MEDIA_URL + 'archive/Galeria/Fotos/Fotos Chamameseros/' + path + url,
						'width':im.size[0],
						'height':im.size[1],
						'name':re.match(pat,url).group(1)
						})
		obj['images'] = img
		return obj

class GaleriaDetailView(generic.DetailView):
	template_name = 'web/galeria.html'
	
	def get_object(self):
		obj = {}
		img = []
		pat = re.compile(ur'(.+)\.(?:png|jpg|PNG|JPG)', re.UNICODE)
		try:
			path = self.kwargs['path']
		except:
			raise Http404("Galeria no existe")
		if path == None:
			path = ''
		path = unicode(path)		
		for url in os.listdir((settings.MEDIA_ROOT + '/archive/Galeria/Fotos/' + path).encode('utf-8')):
			try:
				url = unicode(url.decode('utf-8'))
				im=Image.open((settings.MEDIA_ROOT + 'archive/Galeria/Fotos/' + path + url).encode('utf-8'))
				re.match(pat,url).group(1)
			except:
				continue
			img.append({'url':settings.MEDIA_URL + 'archive/Galeria/Fotos/' + path + url,
						'width':im.size[0],
						'height':im.size[1],
						'name':re.match(pat,url).group(1)
						})
		obj['images'] = img
		obj['name'] = path.replace('/','')
		return obj

class BiografiaView(generic.ListView):
	template_name = 'web/biografias.html'

	def get_queryset(self):
		try:
			filtro = self.kwargs['filtro']
		except:
			filtro = ''
		if (filtro == '') | (filtro == None):
			return Biografia.objects.all().order_by('name__name')
		else:
			return Biografia.objects.filter(name__name__icontains=filtro[:-1]).order_by('name__name')

class BiografiaDetailView(generic.DetailView):
	model = Biografia
	template_name = 'web/biografia.html'

class DiscotecaView(generic.ListView):
	template_name = 'web/discotecas.html'

	def get_queryset(self):
		try:
			filtro = self.kwargs['filtro']
		except:
			filtro = ''
		if (filtro == '') | (filtro == None):
			return Discoteca.objects.all().order_by('name__name')
		else:
			return Discoteca.objects.filter(name__name__icontains=filtro[:-1]).order_by('name__name')

class DiscotecaDetailView(generic.DetailView):
	model = Discoteca
	template_name = 'web/discoteca.html'

class PartituraCView(generic.DetailView):
	template_name = 'web/partituras.html'

	def get_object(self):
		obj = {}
		img = []
		pat = re.compile(ur'(.+)\.(?:png|jpg)', re.UNICODE)

		try:
			path = self.kwargs['path']
		except:
			raise Http404("Galeria no existe")

		if path == None:
			path = ''
		path = unicode(path)

		for url in os.listdir(settings.MEDIA_ROOT + '/archive/Material/Partituras/'):
			try:
				url = unicode(url.decode('utf-8'))
				im=Image.open((settings.MEDIA_ROOT + 'archive/Material/Partituras/' + path + url).encode('utf-8'))
				re.match(pat,url).group(1)
			except:
				continue
			img.append({'url':settings.MEDIA_URL + 'archive/Material/Partituras/' + path + url,
						'width':im.size[0],
						'height':im.size[1],
						'name':re.match(pat,url).group(1)
						})
		obj['images'] = img
		#obj['name'] = (settings.MEDIA_ROOT + 'archive/Cancionero/' + url)
		return obj


class LetrasCView(generic.DetailView):
	template_name = 'web/letras.html'

	def get_object(self):
		obj = {}
		img = []
		pat = re.compile(ur'(.+)\.(?:png|jpg|PNG|JPG)', re.UNICODE)
		try:
			path = self.kwargs['path']
		except:
			raise Http404("Galeria no existe")
		if path == None:
			path = ''
		path = unicode(path)
		for url in os.listdir((settings.MEDIA_ROOT + '/archive/Material/Letras/' + path).encode('utf-8')):
			try:
				url = unicode(url.decode('utf-8'))
				im=Image.open((settings.MEDIA_ROOT + 'archive/Material/Letras/' + path + url).encode('utf-8'))
				re.match(pat,url).group(1)
			except:
				continue
			img.append({'url':settings.MEDIA_URL + 'archive/Material/Letras/' + path + url,
						'width':im.size[0],
						'height':im.size[1],
						'name':re.match(pat,url).group(1)
						})
		obj['images'] = img
		return obj

		
		

def quienesSomos(request):
	return render(request, 'web/quienesSomos.html')

def objetivos(request):
	return render(request, 'web/objetivos.html')

def contacto(request):
	form_class = ContactForm
	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			contact_name = request.POST.get(
				'nombre'
			, '')
			contact_email = request.POST.get(
				'email'
			, '')
			form_content = request.POST.get('mensaje', '')
			email = EmailMessage(
				"Nuevo Mensaje desde la web de Fundacion Memorias del chamame",
				form_content,
				contact_email,
				[settings.DEFAULT_FROM_EMAIL]
			)
			email.send()
			return redirect('contacto')
	return render(request, 'web/contacto.html', {
		'form': form_class,
	})
		
def efemerides(request):
	todayDay = datetime.today().day
	todayMonth = datetime.today().month
	efemerides = Efemeride.objects.filter(date__day=todayDay,date__month=todayMonth)
	efemeridesPorMes = {}
	for efem in EfemerideMes.objects.all():
		efemeridesPorMes[efem.month] = {'efemerides':list(efem.efemeride_set.all().values_list('date','event'))}
	allEfemerides = json.dumps(efemeridesPorMes, cls=DjangoJSONEncoder, ensure_ascii=False)
	return render(request, 'web/efemeride.html', {'efemerides':efemerides,'allEfemerides':allEfemerides})

def benefactores(request):
	return render(request, 'web/benefactores.html')

def construccion(request):
	return render(request, 'web/404.html')

def material(request):
	return render(request, 'web/material.html')

def partituras(request):
	return render(request, 'web/partituras.html')

def cancionero(request):
	return render(request, 'web/cancionero.html')

def error404(request):
	return render(request,'web/404.html')

def error500(request):
	return render(request,'web/500.html')
