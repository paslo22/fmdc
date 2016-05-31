# -*- coding: utf-8 -*- 
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.views import generic
from datetime import datetime
from django.core.mail import EmailMessage
from django.core.serializers.json import DjangoJSONEncoder
from PIL import Image
import os, re, json, random
from .models import Biografia, Efemeride, Discoteca, EfemerideMes, Artista,Actividad
from django.db.models import Q
from .forms import ContactForm
from django.conf import settings

def index(request):
	return render(request, 'web/index.html')

def imgLaterales(request):
	if not request.is_ajax():
		raise Http404('No se puede acceder a esta url.')
	urls = [os.path.join(settings.MEDIA_URL+'Laterales/',fn) for fn in os.listdir(settings.MEDIA_ROOT+'Laterales/')]
	return HttpResponse(json.dumps(random.sample(urls,12), cls=DjangoJSONEncoder, ensure_ascii=False))

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

class VideoView(generic.DetailView):
	template_name = 'web/videoWithLetters.html'

	def get_object(self):
		obj = {}
		img = []
		pat = re.compile(ur'(.+)\.mp4', re.UNICODE)
		try:
			path = self.kwargs['path']
		except:
			raise Http404("Videos no existe")
		if path == None:
			path = ''
		path = unicode(path)
		for url in os.listdir((settings.MEDIA_ROOT + 'archive/Galeria/Videos/' + path).encode('utf-8')):
			try:
				url = unicode(url.decode('utf-8'))
				re.match(pat,url).group(1)
			except:
				continue
			img.append({'url':settings.MEDIA_URL + 'archive/Galeria/Videos/' + path + '/' + url,
						'name':re.match(pat,url).group(1)
						})
		obj['videos'] = img
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
			values = filtro[:-1].split()
			queries = [Q(name__name__icontains=value) for value in values]
			query = queries.pop()
			for item in queries:
				query &= item
			return Biografia.objects.filter(query).order_by('name__name')

class BiografiaDetailView(generic.DetailView):
	model = Biografia
	template_name = 'web/biografia.html'

class BusquedaView(generic.ListView):
	template_name = 'web/busqueda.html'

	def get_queryset(self):
		try:
			filtro = self.kwargs['filtro']
		except:
			filtro = ''
		values = filtro.split()
		queries = [Q(name__icontains=value) for value in values]
		query = queries.pop()
		for item in queries:
			query &= item
		return Artista.objects.filter(query).order_by('name')

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
			values = filtro[:-1].split()
			queries = [Q(name__name__icontains=value) for value in values]
			query = queries.pop()
			for item in queries:
				query &= item
			return Discoteca.objects.filter(query).order_by('name__name')

class DiscotecaDetailView(generic.DetailView):
	model = Discoteca
	template_name = 'web/discoteca.html'

class PartiturasCView(generic.DetailView):
	template_name = 'web/partituras.html'

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
		for url in os.listdir((settings.MEDIA_ROOT + '/archive/Material/Partituras/' + path).encode('utf-8')):
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

class ActividadView(generic.ListView):
	template_name = 'web/actividadesLista.html'

	def get_queryset(self):
		try:
			filtro = self.kwargs['filtro']
		except:
			filtro = ''
		if (filtro == '') | (filtro == None):
			return Actividad.objects.all().order_by('name')
		else:
			values = filtro[:-1].split()
			queries = [Q(name__icontains=value) for value in values]
			query = queries.pop()
			for item in queries:
				query &= item
			return Actividad.objects.filter(query).order_by('name')

	
class ActividadDetailView(generic.DetailView):
	model = Actividad
	template_name = 'web/actividad.html'	


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
			texto = form_content + ' correo enviado por: ' + contact_email
			email = EmailMessage(
				"Nuevo Mensaje desde la web de Fundacion Memorias del chamame",
				texto,
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


