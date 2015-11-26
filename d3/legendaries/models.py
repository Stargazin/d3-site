from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from miscitems.models import Material
from affixes.models import Affix


class LegendaryModel(models.Model):
	name = models.TextField(blank=True)
	name_slug = models.SlugField(blank=True)
	pic = models.ImageField(blank=True)
	slot = models.TextField(blank=True)
	slot_slug = models.SlugField(blank=True)
	category = models.TextField(blank=True)
	category_slug = models.SlugField(blank=True)
	unique = models.TextField(blank=True)
	unique_is_primary = models.NullBooleanField(default=False)
	affixes = models.ManyToManyField(Affix, blank=True)
	random_primaries = models.TextField(blank=True)
	random_secondaries = models.TextField(blank=True)
	owner = models.TextField(blank=True)
	mats = models.ManyToManyField(Material, blank=True)
		##if import problem (circular imports), use str 'miscitems.Material'
	number_of_mats = models.CommaSeparatedIntegerField(max_length=32, blank=True)
	notes = models.TextField(blank=True)

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


class WeaponArmorModel(LegendaryModel):
	inherent = models.TextField(blank=True)

	def slot_singular(self):
		return self.slot

	class Meta:
		abstract = True


@python_2_unicode_compatible
class Weapon(WeaponArmorModel):

	def category_singular(self):
		if self.category == "Ceremonial Knives" or self.category == "Staves":
			if self.category == "Ceremonial Knives":
				return "Ceremonial Knife"
			if self.category == "Staves":
				return "Staff"
		else:
			return self.category[:-1]

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Armor(WeaponArmorModel):

	def category_singular(self):
		return self.category[:-1]

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Accessory(LegendaryModel):

	def category_singular(self):
		return False

	def slot_singular(self):
		return self.slot[:-1]

	def __str__(self):
		return self.name