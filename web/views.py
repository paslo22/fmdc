# -*- coding: utf-8 -*- 
from django.shortcuts import render,redirect
from django.views import generic
from datetime import datetime
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib.staticfiles.templatetags.staticfiles import static
import os, re
from .models import Biografia, Efemeride, Discoteca
from .forms import ContactForm
from django.conf import settings

def index(request):
	return render(request, 'web/index.html')

class GaleriaView(generic.ListView):
	template_name = 'web/galeria.html'

	def get_queryset(self):
		dirlist = os.listdir(settings.MEDIA_ROOT+'/images/')
		dirl = {}
		pat = re.compile(ur'((.+)\.jpg|(.+)\.png)', re.UNICODE)
		try:
			filtro = self.kwargs['filtro'][:-1]
		except:
			filtro = ''
		if (filtro==''):
			for string in dirlist:
				opt = re.match(pat,string)
				dirl[opt.group(2)] = static(settings.MEDIA_URL+'images/'+opt.group(1))
		else:
			for string in dirlist:
				if filtro in string.decode('unicode-escape'):
					opt = re.match(pat,string)
					dirl[opt.group(2)] = static(settings.MEDIA_URL+'images/'+opt.group(1))
		return dirl
	

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
			return Biografia.objects.filter(name__name__contains=filtro[:-1]).order_by('name__name')

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
			return Discoteca.objects.filter(name__name__contains=filtro[:-1]).order_by('name__name')

class DiscotecaDetailView(generic.DetailView):
	model = Discoteca
	template_name = 'web/discoteca.html'

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
	return render(request, 'web/efemeride.html', {'efemerides':efemerides})

def benefactores(request):
	return render(request, 'web/benefactores.html')

def construccion(request):
	return render(request, 'web/404.html')