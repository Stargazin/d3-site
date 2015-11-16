from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class AffixModel(models.Model):
	affix = models.CharField(max_length=255)
	is_primary = models.BooleanField()
	desc = models.TextField()
	ancient = models.TextField(blank=True)
	notes = models.TextField(blank=True)

	class Meta:
		abstract = True

#Armor
#==============================================================================
#==============================================================================
@python_2_unicode_compatible
class HelmetAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Helmet Affixes'

@python_2_unicode_compatible
class SpiritStoneAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Spirit Stone Affixes'

@python_2_unicode_compatible
class VoodooMaskAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Voodoo Mask Affixes'

@python_2_unicode_compatible
class WizardHatAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Wizard Hat Affixes'

@python_2_unicode_compatible
class ShouldersAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Shoulders Affixes'

@python_2_unicode_compatible
class ChestArmorAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Chest Armor Affixes'

@python_2_unicode_compatible
class CloakAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Cloak Affixes'

@python_2_unicode_compatible
class BracersAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Bracers Affixes'

@python_2_unicode_compatible
class GlovesAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Gloves Affixes'

@python_2_unicode_compatible
class BeltAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Belt Affixes'

@python_2_unicode_compatible
class MightyBeltAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Mighty Belt Affixes'

@python_2_unicode_compatible
class PantsAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Pants Affixes'

@python_2_unicode_compatible
class BootsAffix(AffixModel):

	def __str__(self):
		return self.affix

	class Meta:
		verbose_name_plural = 'Boots Affixes'

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
# 		verbose_name_plural = ' Affixes'