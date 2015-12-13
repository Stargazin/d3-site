from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class ItemModel(models.Model):
	name = models.TextField()
	name_slug = models.SlugField(blank=True)
	pic = models.ImageField()
	#Description of item
	unique = models.TextField(blank=True)
	notes = models.TextField(blank=True)

	class Meta:
		abstract = True


@python_2_unicode_compatible
class Potion(ItemModel):
	category = models.TextField(default='Potion')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['pk']


@python_2_unicode_compatible
class Gem(ItemModel):
	rank_unique = models.TextField(blank=True)
	category = models.TextField(default='Gem')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['pk']


@python_2_unicode_compatible
class Material(ItemModel):
	rarity = models.TextField(default='L')
	stack_amount = models.TextField(default='5000')
	category = models.TextField(default='Material')
	#Specific type of material
	slot = models.TextField(blank=True)
	slot_slug = models.SlugField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['pk']