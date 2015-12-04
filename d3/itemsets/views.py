from __future__ import absolute_import

from django.db.models.loading import get_model
from django.views.generic import TemplateView, ListView

from .models import ItemSet, SetEffect, SetPiece


class AllSetsView(ListView):
	template_name = 'itemsets/itemsets_all.html'

	def get_queryset(self):
		model = get_model("itemsets", "ItemSet")
		if self.kwargs['owner_slug'] == 'all':
			self.itemsets = model.objects.all().select_related()
			return self.itemsets
		else:
			self.itemsets = model.objects.filter(owner_slug=self.kwargs['owner_slug']).select_related()

	def get_context_data(self, **kwargs):
		context = super(AllSetsView, self).get_context_data(**kwargs)
		context['itemsets'] = self.itemsets
		return context


class SingleSetView(ListView):
	template_name = 'itemsets/itemsets_single.html'

	def get_queryset(self):
		model = get_model("itemsets", "ItemSet")
		self.itemset = model.objects.select_related().get(name_slug=self.kwargs['name_slug'])
		return self.itemset

	def get_context_data(self, **kwargs):
		context = super(SingleSetView, self).get_context_data(**kwargs)
		context['itemset'] = self.itemset
		return context