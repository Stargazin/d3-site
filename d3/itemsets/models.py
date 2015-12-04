from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from miscitems.models import Material
from affixes.models import Affix


@python_2_unicode_compatible
class ItemSet(models.Model):
	name = models.TextField()
	name_slug = models.SlugField()
	owner = models.TextField()
	owner_slug = models.SlugField()
	notes = models.TextField(blank=True)


	def __str__(self):
		return self.name

	def set_piece(self):
		pic = self.pieces.all()[0].pic
		return pic

	class Meta:
		verbose_name_plural = "Item Sets"


@python_2_unicode_compatible
class SetEffect(models.Model):
	#change to desc?
	effect = models.TextField()
	#change to need or pieces_needed?
	pieces = models.TextField()
	itemSet = models.ForeignKey(ItemSet, related_name='effects')
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.effect

	class Meta:
		verbose_name_plural = "Set Effects"


@python_2_unicode_compatible
class SetPiece(models.Model):
	name = models.TextField()
	name_slug = models.SlugField(blank=True)
	pic = models.ImageField()
	category = models.TextField(blank=True)
	itemSet = models.ForeignKey(ItemSet, related_name='pieces')
	affixes = models.ManyToManyField(Affix, blank=True)
#do this for now instead of primary and secondary random affixes
#just say x Random Magic Properties
	random_affixes = models.TextField(blank=True)
	notes = models.TextField(blank=True)
	# owner = models.TextField(blank=True)
	# mats = models.ManyToManyField(Material, blank=True)
	# number_of_mats = models.CommaSeparatedIntegerField(max_length=32, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Set Pieces"