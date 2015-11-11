from __future__ import absolute_import
	#from .models import x

from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Amulet


def index(request):
	return render(request, 'index.html', {})

def playground(request):
	return render(request, 'playground.html', {})

def amuletsss(request):
	return render(request, 'legendaryitems/amulets.html', {})

def amulets(request):
	context = {}
	items = Amulet.objects.all()
	context['items'] = items
	return render(request, 'legendaryitems.html', context)
