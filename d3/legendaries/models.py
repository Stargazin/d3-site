from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from miscitems.models import Material
from affixes.models import AmuletAffix, RingAffix


class LegendaryModel(models.Model):
	category = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	pic = models.ImageField(blank=True)
	unique = models.TextField(blank=True)
	unique_is_primary = models.NullBooleanField()
	unique2 = models.TextField(blank=True)
	unique2_is_primary = models.NullBooleanField()
	random_primaries = models.CharField(blank=True, max_length=1)
	random_secondaries = models.CharField(blank=True, max_length=1)
	mats = models.ManyToManyField(Material, blank=True)
		##if import problem (circular imports), use str 'miscitems.Material'
	number_of_mats = models.CommaSeparatedIntegerField(max_length=32, blank=True)
	notes = models.TextField(blank=True)
	slug = models.SlugField(blank=True)

	def primary_affixes(self):
		affixes = []
		for affix in self.affixes.all():
			if affix.is_primary:
				affixes.append(affix)
		return affixes

	def secondary_affixes(self):
		affixes = []
		for affix in self.affixes.all():
			if not affix.is_primary:
				affixes.append(affix)
		return affixes

	class Meta:
		abstract = True

	# def uniques(self):
	# 	return self.unique.split("///")
	## usage: {% for unique in item.uniques %}
	##		{{ unique }}
	##		{% endfor %}

class WeaponsModel(LegendaryModel):
	attacks_per_second = models.DecimalField()

	class Meta:
		abstract = True

@python_2_unicode_compatible
class Amulet(LegendaryModel):
	affixes = models.ManyToManyField(AmuletAffix, blank=True)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Ring(LegendaryModel):
	affixes = models.ManyToManyField(RingAffix, blank=True)

	def __str__(self):
		return self.name