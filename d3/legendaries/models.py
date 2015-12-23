from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from miscitems.models import Material
from affixes.models import Affix


class LegendaryModel(models.Model):
	name = models.TextField()
	name_slug = models.SlugField(blank=True)
	pic = models.ImageField()
	#Comes after group
	slot = models.TextField(blank=True)
	slot_slug = models.SlugField(blank=True)
	#Comes after slot
	category = models.TextField(blank=True)
	category_slug = models.SlugField(blank=True)
	#Unique affix of legendary
	unique = models.TextField(blank=True)
	#Unique affix is primary if True, secondary if False
	unique_is_primary = models.NullBooleanField(default=False)
	#Primary and secondary affixes of legendary
	affixes = models.ManyToManyField(Affix, blank=True)
	random_primaries = models.TextField(blank=True)
	random_secondaries = models.TextField(blank=True)
	#Class that uses the legendary
	owner = models.TextField(blank=True)
	#Not in use;
	# mats = models.ManyToManyField(Material, blank=True)
	# 	##If import problem (circular imports), use str 'miscitems.Material'
	# number_of_mats = models.CommaSeparatedIntegerField(max_length=32, blank=True)
	patch = models.TextField()
	notes = models.TextField(blank=True)

	#Get list of primary affixes from all affixes (is_primary = True)
	def primary_affixes(self):
		affixes = []
		for affix in self.affixes.all():
			if affix.is_primary:
				affixes.append(affix)
		return affixes

	#Get list of secondary affixes from all affixes (is_primary = False)
	def secondary_affixes(self):
		affixes = []
		for affix in self.affixes.all():
			if not affix.is_primary:
				affixes.append(affix)
		return affixes

	class Meta:
		abstract = True


class WeaponArmorModel(LegendaryModel):
	#Not in use; attack speed of weapon
	inherent = models.TextField(blank=True)

	class Meta:
		abstract = True


@python_2_unicode_compatible
class Weapon(WeaponArmorModel):
	#Used to get_model in SingleLegendaryView()
	group = models.TextField(default='weapon')

	#Used in single_legendary
	#Singular form of category for legendary type
	def category_singular(self):
		category = self.category
		if category == 'Ceremonial Knives' or category == 'Staves':
			if category == 'Ceremonial Knives':
				return 'Ceremonial Knife'
			if category == 'Staves':
				return 'Staff'
		else:
			return category[:-1]

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['pk']

@python_2_unicode_compatible
class Armor(WeaponArmorModel):
	#Used to get_model in SingleLegendaryView()
	group = models.TextField(default='armor')

	#Used in single_legendary
	def category_singular(self):
		return self.category[:-1]

	#Used in single_legendary; need for legendaries without a category
	def slot_singular(self):
		return self.slot

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Armor'
		ordering = ['pk']

@python_2_unicode_compatible
class Accessory(LegendaryModel):
	#Used to get_model in SingleLegendaryView()
	group = models.TextField(default='accessory')

	#Used in single_legendary
	#Accessories don't have a category
	def category_singular(self):
		return False

	#Used in single_legendary
	def slot_singular(self):
		return self.slot[:-1]

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Accessories'
		ordering = ['pk']