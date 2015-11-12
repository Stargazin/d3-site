from django.db import models
from django.utils.encoding import python_2_unicode_compatible


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

@python_2_unicode_compatible
class RingAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Ring Affixes'