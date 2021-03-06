from __future__ import absolute_import

from django.db.models.loading import get_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import ListView

from .models import ItemSet, SetEffect, SetPiece


class AllSetsView(ListView):
	template_name = 'itemsets/itemsets_all.html'

	#Return all sets as queryset
	def get_queryset(self):
		model = get_model('itemsets', 'ItemSet')
		self.itemsets = get_list_or_404(model.objects.select_related())
		return self.itemsets

	#Return context for template
	def get_context_data(self, **kwargs):
		context = super(AllSetsView, self).get_context_data(**kwargs)
		context['itemsets'] = self.itemsets
		return context


class SingleSetView(ListView):
	template_name = 'itemsets/itemsets_single.html'

	#Return itemset of matching name
	def get_queryset(self):
		model = get_model('itemsets', 'ItemSet')
		self.itemset = get_object_or_404(model.objects.select_related(), name_slug=self.kwargs['name_slug'])
		return self.itemset

	#Return query object for template
	def get_context_data(self, **kwargs):
		context = super(SingleSetView, self).get_context_data(**kwargs)
		context['itemset'] = self.itemset
		return context