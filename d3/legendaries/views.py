from __future__ import absolute_import

from django.db.models.loading import get_model
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import Accessory, Weapon, Armor


class LegendaryView(ListView):
	template_name = 'legendaryitems.html'

	def get_queryset(self):
		if self.kwargs['model'] == 'weapons':
			self.kwargs['model'] = 'weapon'
		if self.kwargs['model'] == 'accessories':
			self.kwargs['model'] = 'accessory'
		model = get_model("legendaries", self.kwargs['model'])
		self.items = model.objects.all()
		return self.items

	def get_context_data(self, **kwargs):
		context = super(LegendaryView, self).get_context_data(**kwargs)
		context['items'] = self.items
		return context

class SlotView(LegendaryView):

	def get_queryset(self):
		if self.kwargs['model'] == 'weapons':
			self.kwargs['model'] = 'weapon'
		if self.kwargs['model'] == 'accessories':
			self.kwargs['model'] = 'accessory'
		model = get_model("legendaries", self.kwargs['model'])
		self.items = model.objects.filter(slot_slug=self.kwargs['slot_slug'])
		return self.items

class CategoryView(LegendaryView):

	def get_queryset(self):
		if self.kwargs['model'] == 'weapons':
			self.kwargs['model'] = 'weapon'
		model = get_model("legendaries", self.kwargs['model'])
		self.items = model.objects.filter(category_slug=self.kwargs['category_slug'])
		return self.items












class PlaygroundView(TemplateView):
	template_name = "playground.html"
