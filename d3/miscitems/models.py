from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Material(models.Model):
	name = models.CharField(max_length=255)
	pic = models.ImageField(blank=True)
	rarity = models.CharField(max_length=255)
	stack_amount = models.IntegerField(default=5000)
	desc = models.TextField(blank=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.name