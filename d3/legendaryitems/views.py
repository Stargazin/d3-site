from __future__ import absolute_import
	#from .models import x

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):
	return render(request, 'index.html', {})

def playground(request):
	return render(request, 'playground.html', {})

def amulets(request):
	return render(request, 'legendaryitems/amulets.html', {})

# def legendary_amulets(request):
# 	