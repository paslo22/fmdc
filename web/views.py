from django.shortcuts import render
from django.views import generic
from .models import Biografia

def index(request):
	return render(request, 'web/index.html')

class BiografiaView(generic.ListView):
	template_name = 'web/biografias.html'

	def get_queryset(self):
		return Biografia.objects.all()

class BiografiaDetailView(generic.DetailView):
	model = Biografia
	template_name = 'web/biografia.html'