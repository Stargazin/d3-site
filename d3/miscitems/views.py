from __future__ import absolute_import

from django.db.models.loading import get_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import ListView

from .models import Gem, Potion, Material


class AllContextMixin(object):
	context_object_name = 'items'


class GemView(ListView):
	template_name = 'items/items_gems.html'

	def get_queryset(self):
		model = get_model('miscitems', 'Gem')
		self.items = get_list_or_404(model)
		return self.items

	def get_context_data(self, **kwargs):
		context = super(GemView, self).get_context_data(**kwargs)
		context['items'] = self.items
		context['header'] = self.items[0].category
		return context


class PotionView(ListView):
	template_name = 'items/items_potions.html'

	def get_queryset(self):
		model = get_model('miscitems', 'Potion')
		self.items = get_list_or_404(model)
		return self.items

	def get_context_data(self, **kwargs):
		context = super(PotionView, self).get_context_data(**kwargs)
		context['items'] = self.items
		context['header'] = self.items[0].category
		return context


class MaterialView(ListView):
	template_name = 'items/items_materials.html'

	def get_queryset(self):
		model = get_model('miscitems', 'Material')
		self.items = get_list_or_404(model)
		return self.items

	def get_context_data(self, **kwargs):
		context = super(MaterialView, self).get_context_data(**kwargs)
		context['items'] = self.items
		context['header'] = self.items[0].category
		return context


class SlotMaterialView(ListView):
	template_name = 'items/items_materials.html'

	def get_queryset(self):
		self.items = get_list_or_404(Material.objects, slot_slug=self.kwargs['slot_slug'])
		return self.items

	def get_context_data(self, **kwargs):
		context = super(SlotMaterialView, self).get_context_data(**kwargs)
		context['items'] = self.items
		context['header'] = self.items[0].slot
		return context


class SingleMiscView(ListView):

	def get_queryset(self):
		model = get_model('miscitems', self.model)
		self.item = get_object_or_404(model, name_slug=self.kwargs['name_slug'])
		return self.item

	def get_context_data(self, **kwargs):
		context = super(SingleMiscView, self).get_context_data(**kwargs)
		context['item'] = self.item
		return context


class SingleGemView(SingleMiscView):
	template_name = 'single/single_gem.html'

	def __init__(self):
		super(SingleGemView, self).__init__()
		self.model = 'Gem'


class SinglePotionView(SingleMiscView):
	template_name = 'single/single_potion.html'

	def __init__(self):
		super(SinglePotionView, self).__init__()
		self.model = 'Potion'


class SingleMaterialView(SingleMiscView):
	template_name = 'single/single_material.html'

	def __init__(self):
		super(SingleMaterialView, self).__init__()
		self.model = 'Material'