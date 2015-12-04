from __future__ import absolute_import

from django.db.models.loading import get_model
# from django.http import HttpResponse
# from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import Accessory, Weapon, Armor


class WeaponMixin(object):

	def __init__(self, *args, **kwargs):
		self.group = 'Weapon'

class ArmorMixin(object):

	def __init__(self, *args, **kwargs):
		self.group = 'Armor'

class AccessoryMixin(object):

	def __init__(self, *args, **kwargs):
		self.group = 'Accessory'


class GroupView(ListView):
	template_name = 'items/items_legendaries.html'

	def get_queryset(self):
		model = get_model("legendaries", self.group)
		self.items = model.objects.all()
		# self.items = get_list_or_404(model)
		return self.items

	def get_context_data(self, **kwargs):
		context = super(GroupView, self).get_context_data(**kwargs)
		context['items'] = self.items
		return context


class GroupWeaponView(WeaponMixin, GroupView):
	pass

class GroupArmorView(ArmorMixin, GroupView):
	pass

class GroupAccessoryView(AccessoryMixin, GroupView):
	pass


class SlotView(GroupView):

	def get_queryset(self):
		model = get_model("legendaries", self.group)
		self.items = model.objects.filter(slot_slug=self.kwargs['slot_slug'])
		return self.items

class SlotWeaponView(WeaponMixin, SlotView):
	pass

class SlotArmorView(ArmorMixin, SlotView):
	pass

class SlotAccessoryView(AccessoryMixin, SlotView):
	pass


class CategoryView(GroupView):

	def get_queryset(self):
		model = get_model("legendaries", self.group)
		self.items = model.objects.filter(category_slug=self.kwargs['category_slug'])
		return self.items

class CategoryWeaponView(WeaponMixin, CategoryView):
	pass

class CategoryArmorView(ArmorMixin, CategoryView):
	pass



class SingleLegendaryView(ListView):
	template_name = 'single/single_legendary.html'

	def get_queryset(self):
		model = get_model("legendaries", self.kwargs['group'])
		self.item = model.objects.get(name_slug=self.kwargs['name_slug'])
		# self.item = model.objects.select_related().get()
		return self.item

	def get_context_data(self, **kwargs):
		context = super(SingleLegendaryView, self).get_context_data(**kwargs)
		context['item'] = self.item
		return context