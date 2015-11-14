from __future__ import absolute_import

from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import TemplateView

from .models import Amulet, Ring, Source, CrusaderShield, Mojo, Quiver, Shield


class PlaygroundView(TemplateView):
	template_name = "playground.html"



class LegendaryItemsMixin(object):
	template_name = "legendaryitems.html"

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

# class FollowerRelicsView(LegendaryItemsMixin, TemplateView):
# 	def get_context_data(self, **kwargs):
# 		context = super(FollowerRelicsView, self).get_context_data(**kwargs)
# 		context['items'] = FollowerRelic.objects.all()
# 		return context


# class ||View(LegendaryItemsMixin, TemplateView):
# 	def get_context_data(self, **kwargs):
# 		context = super(||View, self).get_context_data(**kwargs)
# 		context['items'] = ||.objects.all()
# 		return context