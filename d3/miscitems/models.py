from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class ItemModel(models.Model):
	name = models.TextField(blank=True)
	name_slug = models.SlugField(blank=True)
	pic = models.ImageField(blank=True)
	unique = models.TextField(blank=True)
	notes = models.TextField(blank=True)

	class Meta:
		abstract = True


@python_2_unicode_compatible
class Potion(ItemModel):
	# slot = models.TextField(default='Legendary Potion')

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Gem(ItemModel):
	rank_unique = models.TextField(blank=True)
	# slot = models.TextField(default='Legendary Gem')

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Material(ItemModel):
	rarity = models.TextField(default='L')
	stack_amount = models.TextField(default='5000')
	category = models.TextField(blank=True)
	category_slug = models.SlugField(blank=True)

	def __str__(self):
		return self.name