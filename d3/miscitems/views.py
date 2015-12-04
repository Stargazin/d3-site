from __future__ import absolute_import

from django.db.models.loading import get_model
# from django.http import HttpResponse
# from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView

from .models import Gem, Potion, Material


class AllContextMixin(object):
	context_object_name = 'items'


class GemView(AllContextMixin, ListView):
	template_name = 'items/items_gems.html'
	model = Gem

	# def __init__(self, *args, **kwargs):
	# 	super(GemView, self).__init__()
	# 	self.model = Gem

class PotionView(AllContextMixin, ListView):
	template_name = 'items/items_potions.html'
	model = Potion


class MaterialView(AllContextMixin, ListView):
	template_name = 'items/items_materials.html'
	model = Material


class CategoryMaterialView(ListView):
	template_name = "items/items_materials.html"

	def get_queryset(self):
		self.items = Material.objects.filter(category_slug=self.kwargs["category_slug"])
		return self.items

	def get_context_data(self, **kwargs):
		context = super(CategoryMaterialView, self).get_context_data(**kwargs)
		context['items'] = self.items
		return context



class SingleMiscView(ListView):

	def get_queryset(self):
		model = get_model("miscitems", self.model)
		self.item = model.objects.get(name_slug=self.kwargs['name_slug'])
		return self.item

	def get_context_data(self, **kwargs):
		context = super(SingleMiscView, self).get_context_data(**kwargs)
		context['item'] = self.item
		return context

class SingleGemView(SingleMiscView):
	template_name = 'single/single_gem.html'

	def __init__(self):
		super(SingleGemView, self).__init__()
		self.model = "Gem"

class SinglePotionView(SingleMiscView):
	template_name = 'single/single_potion.html'

	def __init__(self):
		super(SinglePotionView, self).__init__()
		self.model = "Potion"

class SingleMaterialView(SingleMiscView):
	template_name = 'single/single_material.html'

	def __init__(self):
		super(SingleMaterialView, self).__init__()
		self.model = "Material"






class MiscView(AllContextMixin, ListView):
	template_name = 'misc.html'