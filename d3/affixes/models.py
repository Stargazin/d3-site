from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Affix(models.Model):
	##Slot and category used to relate to foreign keys
	slot = models.TextField(blank=True)
	category = models.TextField(blank=True)
	affix = models.TextField(unique=False)
	#Affix is primary if True, secondary if False
	is_primary = models.BooleanField()
	#Details of Affix
	desc = models.TextField()
	#Ancient version of affix desc; default = desc
	ancient = models.TextField(blank=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Affixes'