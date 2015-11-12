from __future__ import absolute_import
	#from .models import x

from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import TemplateView

from .models import Amulet


class PlaygroundView(TemplateView):
	template_name = "playground.html"


class LegendaryItemsMixin(object):
	template_name = "legendaryitems.html"

class AmuletsView(LegendaryItemsMixin, TemplateView):
	def get_context_data(self, **kwargs):
		context = super(AmuletsView, self).get_context_data(**kwargs)
		context['items'] = Amulet.objects.all()
		return context

# class RingsView(LegendaryItemsMixin, TemplateView):
# 	def get_context_data(self, **kwargs):
# 		context = super(RingsView, self).get_context_data(**kwargs)
# 		context['items'] = Ring.objects.all()
# 		return context

# class FollowerRelicsView(LegendaryItemsMixin, TemplateView):
# 	def get_context_data(self, **kwargs):
# 		context = super(FollowerRelicsView, self).get_context_data(**kwargs)
# 		context['items'] = FollowerRelic.objects.all()
# 		return context


# class View(LegendaryItemsMixin, TemplateView):
# 	def get_context_data(self, **kwargs):
# 		context = super(||View, self).get_context_data(**kwargs)
# 		context['items'] = ||.objects.all()
# 		return context