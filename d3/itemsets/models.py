from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from miscitems.models import Material
from affixes.models import AccessoryAffix, WeaponAffix, ArmorAffix


@python_2_unicode_compatible
class ItemSet(models.Model):
	name = models.TextField()
	name_slug = models.SlugField()
	#barb, sader, dh, monk, wd, wiz, all
	owner = models.TextField()
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class SetEffect(models.Model):
	effect = models.TextField()
	pieces = models.TextField()
	itemSet = models.ForeignKey(ItemSet)
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.effect


@python_2_unicode_compatible
class SetPiece(models.Model):
	name = models.TextField()
	name_slug = models.SlugField(blank=True)
	pic = models.ImageField()
	category = models.TextField(blank=True)
	itemSet = models.ForeignKey(ItemSet)
	# affixes = models.ManyToManyField(Affix, blank=True)
#do this for now instead of primary and secondary random affixes
#just say x Random Magic Properties
	random_affixes = 
	notes = models.TextField(blank=True)
#pull owner from itemSet.owner
	# mats = models.ManyToManyField(Material, blank=True)
	# number_of_mats = models.CommaSeparatedIntegerField(max_length=32, blank=True)

	def __str__(self):
		return self.name