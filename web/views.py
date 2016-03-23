from django.shortcuts import render
from django.views import generic
from datetime import datetime
from .models import Biografia, Efemeride

def index(request):
	return render(request, 'web/index.html')

class BiografiaView(generic.ListView):
	template_name = 'web/biografias.html'

	def get_queryset(self):
		return Biografia.objects.all()

class BiografiaDetailView(generic.DetailView):
	model = Biografia
	template_name = 'web/biografia.html'

def quienesSomos(request):
	return render(request, 'web/quienesSomos.html')

def objetivos(request):
	return render(request, 'web/objetivos.html')

def contacto(request):
	return render(request, 'web/contacto.html')

def efemerides(request):
	todayDay = datetime.today().day
	todayMonth = datetime.today().month
	efemerides = Efemeride.objects.filter(date__day=todayDay,date__month=todayMonth)
	return render(request, 'web/efemeride.html', {'efemerides':efemerides})

def benefactores(request):
	return render(request, 'web/benefactores.html')