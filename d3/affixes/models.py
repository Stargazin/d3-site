from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class AffixModel(models.Model):
	affix = models.CharField(max_length=255)
	is_primary = models.BooleanField()
	desc = models.TextField()
	ancient = models.TextField(blank=True)

	class Meta:
		abstract = True

#Armor
#==============================================================================
#==============================================================================

# @python_2_unicode_compatible
# class Affix(AffixModel):

# 	def __str__(self):
# 		return self.affix

# 	class Meta:
# 		verbose_name_plural = 'Affixes'

#Accessories
#==============================================================================
#==============================================================================
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

#Off-Hands
#==============================================================================
#==============================================================================
@python_2_unicode_compatible
class SourceAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Source Affixes'

@python_2_unicode_compatible
class CrusaderShieldAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Crusader Shield Affixes'

@python_2_unicode_compatible
class MojoAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Mojo Affixes'

@python_2_unicode_compatible
class QuiverAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Quiver Affixes'

@python_2_unicode_compatible
class ShieldAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Shield Affixes'

#Weapons
#==============================================================================
#==============================================================================


# @python_2_unicode_compatible
# class Affix(AffixModel):

# 	def __str__(self):
# 		return self.affix

# 	class Meta:
# 		verbose_name_plural = 'Affixes'