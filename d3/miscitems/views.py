from __future__ import absolute_import

from django.db.models.loading import get_model
# from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView

from .models import Gem, Potion, Material


class TemplateMixin(object):
	template_name = 'legendarymisc.html'
	context_object_name = 'items'

class GemView(TemplateMixin, ListView):
	model = Gem

class PotionView(TemplateMixin, ListView):
	model = Potion

class MaterialView(TemplateMixin, ListView):
	model = Material