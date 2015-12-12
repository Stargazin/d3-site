from __future__ import absolute_import

from django.db.models.loading import get_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import ListView

from .models import ItemSet, SetEffect, SetPiece


class AllSetsView(ListView):
	template_name = 'itemsets/itemsets_all.html'

	def get_queryset(self):
		model = get_model('itemsets', 'ItemSet')
		if self.kwargs['owner_slug'] == 'all':
			self.itemsets = get_list_or_404(model.objects.select_related())
			return self.itemsets
		else:
			self.itemsets = get_list_or_404(model.objects.select_related(), owner_slug=self.kwargs['owner_slug'])
			return self.itemsets

	def get_context_data(self, **kwargs):
		context = super(AllSetsView, self).get_context_data(**kwargs)
		context['itemsets'] = self.itemsets
		if self.itemsets[0].owner == 'Universal':
			context['header'] = 'Item'
		else:
			context['header'] = self.itemsets[0].owner
		return context


class SingleSetView(ListView):
	template_name = 'itemsets/itemsets_single.html'

	def get_queryset(self):
		model = get_model('itemsets', 'ItemSet')
		self.itemset = get_object_or_404(model.objects.select_related(), name_slug=self.kwargs['name_slug'])
		return self.itemset

	def get_context_data(self, **kwargs):
		context = super(SingleSetView, self).get_context_data(**kwargs)
		context['itemset'] = self.itemset
		return context