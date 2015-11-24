from __future__ import absolute_import

from django.db.models.loading import get_model
# from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView

from .models import Gem, Potion, Material


class ContextMixin(object):
	context_object_name = 'items'

class GemView(ContextMixin, ListView):
	template_name = 'gems.html'
	model = Gem

class PotionView(ContextMixin, ListView):
	template_name = 'potions.html'
	model = Potion

class MaterialView(ContextMixin, ListView):
	template_name = 'materials.html'
	model = Material

class MaterialCategoryView(ListView):
	template_name = "materialscategory.html"

	def get_queryset(self):
		self.items = Material.objects.filter(category_slug=self.kwargs["category_slug"])
		return self.items

	def get_context_data(self, **kwargs):
		context = super(MaterialCategoryView, self).get_context_data(**kwargs)
		context['items'] = self.items
		return context