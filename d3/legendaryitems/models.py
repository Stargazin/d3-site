from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from miscitems.models import Material


class AffixModel(models.Model):
	affix = models.CharField(max_length=255)
	is_primary = models.BooleanField()
	desc = models.TextField()
	ancient = models.TextField(blank=True)

	class Meta:
		abstract = True

@python_2_unicode_compatible
class AmuletAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Amulet Affixes'


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

	##not sure why but this doesn't work
	## def save(self, *args, **kwargs):
	## 	self.slug = slugify(self.name)
	## 	super(Amulet, self).save(*args, **kwargs)

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

	def __str__(self):
		return self.name