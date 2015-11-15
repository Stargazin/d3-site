from __future__ import absolute_import

from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import TemplateView

from .models import Helmet, SpiritStone, VoodooMask, WizardHat, Shoulders, ChestArmor, Cloak, Bracers, Gloves, Belt, MightyBelt, Pants, Boots, Amulet, Ring, Source, CrusaderShield, Mojo, Quiver, Shield


class PlaygroundView(TemplateView):
	template_name = "playground.html"


class LegendaryItemsMixin(object):
	template_name = "legendaryitems.html"

#Armor
#==============================================================================
#==============================================================================
class HelmetView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(HelmetView, self).get_context_data(**kwargs)
		context['items'] = Helmet.objects.all()
		return context

class SpiritStoneView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(SpiritStoneView, self).get_context_data(**kwargs)
		context['items'] = SpiritStone.objects.all()
		return context

class VoodooMaskView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(VoodooMaskView, self).get_context_data(**kwargs)
		context['items'] = VoodooMask.objects.all()
		return context

class WizardHatView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(WizardHatView, self).get_context_data(**kwargs)
		context['items'] = WizardHat.objects.all()
		return context


class ShouldersView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(ShouldersView, self).get_context_data(**kwargs)
		context['items'] = Shoulders.objects.all()
		return context


class ChestArmorView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(ChestArmorView, self).get_context_data(**kwargs)
		context['items'] = ChestArmor.objects.all()
		return context

class CloakView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(CloakView, self).get_context_data(**kwargs)
		context['items'] = Cloak.objects.all()
		return context


class BracersView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(BracersView, self).get_context_data(**kwargs)
		context['items'] = Bracers.objects.all()
		return context


class GlovesView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(GlovesView, self).get_context_data(**kwargs)
		context['items'] = Gloves.objects.all()
		return context


class BeltView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(BeltView, self).get_context_data(**kwargs)
		context['items'] = Belt.objects.all()
		return context

class MightyBeltView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(MightyBeltView, self).get_context_data(**kwargs)
		context['items'] = MightyBelt.objects.all()
		return context


class PantsView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(PantsView, self).get_context_data(**kwargs)
		context['items'] = Pants.objects.all()
		return context


class BootsView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(BootsView, self).get_context_data(**kwargs)
		context['items'] = Boots.objects.all()
		return context

#Accessories
#==============================================================================
#==============================================================================
class AmuletView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(AmuletView, self).get_context_data(**kwargs)
		context['items'] = Amulet.objects.all()
		context['pic'] = 1
		return context

class RingView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(RingView, self).get_context_data(**kwargs)
		context['items'] = Ring.objects.all()
		context['pic'] = 1
		return context

# class FollowerRelicView(LegendaryItemsMixin, TemplateView):
# 	def get_context_data(self, **kwargs):
# 		context = super(FollowerRelicView, self).get_context_data(**kwargs)
# 		context['items'] = FollowerRelic.objects.all()
# 		return context

#Off-Hands
#==============================================================================
#==============================================================================
class SourceView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(SourceView, self).get_context_data(**kwargs)
		context['items'] = Source.objects.all()
		return context

class CrusaderShieldView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(CrusaderShieldView, self).get_context_data(**kwargs)
		context['items'] = CrusaderShield.objects.all()
		return context

class MojoView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(MojoView, self).get_context_data(**kwargs)
		context['items'] = Mojo.objects.all()
		return context

class QuiverView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(QuiverView, self).get_context_data(**kwargs)
		context['items'] = Quiver.objects.all()
		return context

class ShieldView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(ShieldView, self).get_context_data(**kwargs)
		context['items'] = Shield.objects.all()
		return context


# class ||View(LegendaryItemsMixin, TemplateView):
# 	def get_context_data(self, **kwargs):
# 		context = super(||View, self).get_context_data(**kwargs)
# 		context['items'] = ||.objects.all()
# 		return context