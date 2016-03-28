from django.shortcuts import render,redirect
from django.views import generic
from datetime import datetime
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from .models import Biografia, Efemeride
from .forms import ContactForm
from django.conf import settings
from .models import Biografia, Efemeride, Discoteca

def index(request):
	return render(request, 'web/index.html')

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
				"Nuevo Mensaje desde la web",
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