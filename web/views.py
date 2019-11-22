# -*- coding: utf-8 -*-
import os
import json
import random

from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views import generic
from datetime import datetime
from django.core.mail import EmailMessage
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.conf import settings

from .forms import ContactForm
from .models import Biografia, Efemeride, Discoteca, EfemerideMes, Artista, Actividad
from web.constants import IMAGE_EXTENSION_PATTERN, MP4_EXTENSION_PATTERN
from web.helpers import get_files_from_folder_path


def index(request):
    return render(request, 'web/index.html')


def imgLaterales(request):
    if not request.is_ajax():
        raise Http404('No se puede acceder a esta url.')
    urls = [os.path.join(settings.MEDIA_URL + 'Laterales/', fn) for fn in os.listdir(settings.MEDIA_ROOT+'Laterales/')]
    return HttpResponse(json.dumps(random.sample(urls, 12), cls=DjangoJSONEncoder, ensure_ascii=False))


class GaleriaView(generic.ListView):
    template_name = 'web/galerias.html'

    def get_queryset(self):
        return {
            'images': os.listdir(settings.MEDIA_ROOT+'/archive/Galeria/Fotos'),
            'videos': os.listdir(settings.MEDIA_ROOT+'/archive/Galeria/Videos'),
        }


class GaleriaCView(generic.DetailView):
    template_name = 'web/galeriaWithLetters.html'

    def get_object(self):
        obj = {}
        folder_letter = self.kwargs['path']
        if folder_letter is None:
            return obj
        path = '/archive/Galeria/Fotos/Fotos Chamameseros/' + folder_letter
        music_sheet_images = get_files_from_folder_path(path=path, pattern=IMAGE_EXTENSION_PATTERN)
        obj['images'] = music_sheet_images[0:4]
        obj['lazyImages'] = music_sheet_images[4:]
        return obj


class GaleriaDetailView(generic.DetailView):
    template_name = 'web/galeria.html'

    def get_object(self):
        obj = {}
        obj = {}
        folder_letter = self.kwargs['path']
        if folder_letter is None:
            return obj
        path = '/archive/Galeria/Fotos/' + folder_letter
        print(folder_letter)
        gallery_images = get_files_from_folder_path(path=path, pattern=IMAGE_EXTENSION_PATTERN)
        obj['images'] = gallery_images[0:4]
        obj['lazyImages'] = gallery_images[4:]
        obj['name'] = folder_letter.replace('/', '')
        return obj


class VideoView(generic.DetailView):
    template_name = 'web/videoWithLetters.html'

    def get_object(self):
        obj = {}
        folder_letter = self.kwargs['path']
        if folder_letter is None:
            return obj
        path = '/archive/Galeria/Videos/' + folder_letter
        videos = get_files_from_folder_path(path=path, pattern=MP4_EXTENSION_PATTERN)
        obj['videos'] = videos
        return obj


class BiografiaView(generic.ListView):
    template_name = 'web/biografias.html'

    def get_queryset(self):
        filtro = self.kwargs.get('filtro', None)
        if filtro is None:
            return Biografia.objects.all().order_by('name__name')
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
        lookup_filter = self.kwargs.get('filtro', None)
        values = lookup_filter.split()
        queries = [Q(name__icontains=value) for value in values]
        query = queries.pop()
        for item in queries:
            query &= item
        return Artista.objects.filter(query).order_by('name')


class DiscotecaView(generic.ListView):
    template_name = 'web/discotecas.html'

    def get_queryset(self):
        lookup_filter = self.kwargs.get('filtro', None)
        if lookup_filter is None:
            return Discoteca.objects.all().order_by('name__name')
        filter_without_backslash = lookup_filter[:-1].split()
        return Discoteca.objects.filter(
            name__name__icontains=filter_without_backslash).order_by('name__name')


class DiscotecaDetailView(generic.DetailView):
    model = Discoteca
    template_name = 'web/discoteca.html'


class PartiturasCView(generic.DetailView):
    template_name = 'web/partituras.html'

    def get_object(self):
        obj = {}
        folder_letter = self.kwargs['path']
        if folder_letter is None:
            return obj
        path = '/archive/Material/Partituras/' + folder_letter
        music_sheet_images = get_files_from_folder_path(path=path, pattern=IMAGE_EXTENSION_PATTERN)
        obj['images'] = music_sheet_images
        return obj


class LetrasCView(generic.DetailView):
    template_name = 'web/letras.html'

    def get_object(self):
        obj = {}
        folder_letter = self.kwargs['path']
        if folder_letter is None:
            return obj
        path = '/archive/Material/Letras/' + folder_letter
        lyrics_images = get_files_from_folder_path(path=path, pattern=IMAGE_EXTENSION_PATTERN)
        obj['images'] = lyrics_images
        return obj


class ActividadView(generic.ListView):
    template_name = 'web/actividadesLista.html'

    def get_queryset(self):
        lookup_filter = self.kwargs.get('filtro', None)
        if lookup_filter is None:
            return Actividad.objects.all().order_by('name')
        filter_without_backslash = lookup_filter[:-1].strip()
        return Actividad.objects.filter(
            name__icontains=filter_without_backslash).order_by('name')


class ActividadDetailView(generic.DetailView):
    model = Actividad
    template_name = 'web/actividad.html'


def consejoAdm(request):
    return render(request, 'web/quienesSomos.html')

def consejoCon(request):
    return render(request, 'web/consejoCon.html')

def miembros(request):
    return render(request, 'web/miembros.html')

def objetivos(request):
    return render(request, 'web/objetivos.html')


def contacto(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get(
                'nombre', '')
            contact_email = request.POST.get(
                'email', '')
            form_content = request.POST.get('mensaje', '')
            texto = form_content + ' correo enviado por: ' + contact_name
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
    efemerides = Efemeride.objects.filter(date__day=todayDay, date__month=todayMonth)
    efemeridesPorMes = {}
    for efem in EfemerideMes.objects.all():
        efemeridesPorMes[efem.month] = {'efemerides': list(efem.efemeride_set.all().values_list('date', 'event'))}
    allEfemerides = json.dumps(efemeridesPorMes, cls=DjangoJSONEncoder, ensure_ascii=False)
    return render(request, 'web/efemeride.html', {'efemerides': efemerides, 'allEfemerides': allEfemerides})


def benefactores(request):
    return render(request, 'web/benefactores.html')

def material(request):
    return render(request, 'web/material.html')


def partituras(request):
    return render(request, 'web/partituras.html')


def cancionero(request):
    return render(request, 'web/cancionero.html')


def error404(request, exception=None):
    return render(request, 'web/404.html')


def error500(request, exception=None):
    return render(request, 'web/500.html')
