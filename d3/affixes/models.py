from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class AffixModel(models.Model):
	slot = models.TextField(blank=True)
	category = models.TextField(blank=True)
	affix = models.TextField(unique=False)
	is_primary = models.BooleanField()
	desc = models.TextField()
	ancient = models.TextField(blank=True)
	notes = models.TextField(blank=True)

	class Meta:
		abstract = True


@python_2_unicode_compatible
class AccessoryAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Accessory Affixes'

@python_2_unicode_compatible
class WeaponAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Weapon Affixes'

@python_2_unicode_compatible
class ArmorAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Armor Affixes'