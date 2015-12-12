from __future__ import absolute_import

from django.db.models.loading import get_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import ListView

from .models import Accessory, Weapon, Armor


class ItemsTemplateMixin(object):
	template_name = 'items/items_legendaries.html'

class WeaponMixin(object):

	def __init__(self, *args, **kwargs):
		self.group = 'Weapon'
		self.group_header = 'Weapons'

class ArmorMixin(object):

	def __init__(self, *args, **kwargs):
		self.group = 'Armor'
		self.group_header = 'Armor'

class AccessoryMixin(object):

	def __init__(self, *args, **kwargs):
		self.group = 'Accessory'
		self.group_header = 'Accessories'


class AllLegendariesView(ItemsTemplateMixin, ListView):

	def get_queryset(self):
		weapons = get_model('legendaries', 'Weapon')
		armor = get_model('legendaries', 'Armor')
		accessories = get_model('legendaries', 'Accessory')
		self.items = []
		for weapon in weapons.objects.all():
			self.items.append(weapon)
		for armor in armor.objects.all():
			self.items.append(armor)
		for accessory in accessories.objects.all():
			self.items.append(accessory)
		return self.items

	def get_context_data(self, **kwargs):
		context = super(AllLegendariesView, self).get_context_data(**kwargs)
		context['items'] = self.items
		context['header'] = 'Legendary Items'
		context['title'] = 'Legendary Items'
		return context


class GroupView(ItemsTemplateMixin, ListView):

	def get_queryset(self):
		model = get_model('legendaries', self.group)
		self.items = get_list_or_404(model)
		return self.items

	def get_context_data(self, **kwargs):
		context = super(GroupView, self).get_context_data(**kwargs)
		context['items'] = self.items
		context['header'] = self.group_header
		context['title'] = 'Legendary ' + self.group_header
		return context

class GroupWeaponView(WeaponMixin, GroupView):
	pass

class GroupArmorView(ArmorMixin, GroupView):
	pass

class GroupAccessoryView(AccessoryMixin, GroupView):
	pass


class SlotView(ItemsTemplateMixin, ListView):

	def get_queryset(self):
		model = get_model('legendaries', self.group)
		self.items = get_list_or_404(model, slot_slug=self.kwargs['slot_slug'])
		return self.items

	def get_context_data(self, **kwargs):
		context = super(SlotView, self).get_context_data(**kwargs)
		context['items'] = self.items
		context['header'] = self.items[0].slot
		context['title'] = 'Legendary ' + self.items[0].slot
		return context

class SlotWeaponView(WeaponMixin, SlotView):
	pass

class SlotArmorView(ArmorMixin, SlotView):
	pass

class SlotAccessoryView(AccessoryMixin, SlotView):
	pass


class CategoryView(ItemsTemplateMixin, ListView):

	def get_queryset(self):
		model = get_model('legendaries', self.group)
		self.items = get_list_or_404(model, category_slug=self.kwargs['category_slug'])
		return self.items

	def get_context_data(self, **kwargs):
		context = super(CategoryView, self).get_context_data(**kwargs)
		context['items'] = self.items
		context['header'] = self.items[0].category
		context['title'] = 'Legendary ' + self.items[0].category
		return context

class CategoryWeaponView(WeaponMixin, CategoryView):
	pass

class CategoryArmorView(ArmorMixin, CategoryView):
	pass


class SingleLegendaryView(ListView):
	template_name = 'single/single_legendary.html'

	def get_queryset(self):
		model = get_model('legendaries', self.kwargs['group'])
		self.item = get_object_or_404(model, name_slug=self.kwargs['name_slug'])
		return self.item

	def get_context_data(self, **kwargs):
		context = super(SingleLegendaryView, self).get_context_data(**kwargs)
		context['item'] = self.item
		return context