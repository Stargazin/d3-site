from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from miscitems.models import Material
from affixes.models import HelmetAffix, SpiritStoneAffix, VoodooMaskAffix, WizardHatAffix, ShouldersAffix, ChestArmorAffix, CloakAffix, BracersAffix, GlovesAffix, BeltAffix, MightyBeltAffix, PantsAffix, BootsAffix, AmuletAffix, RingAffix, SourceAffix, CrusaderShieldAffix, MojoAffix, QuiverAffix, ShieldAffix


class LegendaryModel(models.Model):
	category = models.CharField(max_length=255, blank=True)
	###slot = models.TextField(default="")
	name = models.CharField(max_length=255)
	pic = models.ImageField(blank=True)
	unique = models.TextField(blank=True)
	unique_is_primary = models.NullBooleanField(default=False)
	unique2 = models.TextField(blank=True)
	unique2_is_primary = models.NullBooleanField(default=False)
	unique3 = models.TextField(blank=True)
	unique3_is_primary = models.NullBooleanField(default=False)
	random_primaries = models.CharField(blank=True, max_length=1)
	random_secondaries = models.CharField(blank=True, max_length=1)
	mats = models.ManyToManyField(Material, blank=True)
		##if import problem (circular imports), use str 'miscitems.Material'
	number_of_mats = models.CommaSeparatedIntegerField(max_length=32, blank=True)
	notes = models.TextField(blank=True)
	slug = models.SlugField(blank=True)

	def primary_affixes(self):
		affixes = []
		for affix in self.affixes.all():
			if affix.is_primary:
				affixes.append(affix)
		return affixes

	def secondary_affixes(self):
		affixes = []
		for affix in self.affixes.all():
			if not affix.is_primary:
				affixes.append(affix)
		return affixes

	class Meta:
		abstract = True

#Armor
#==============================================================================
#==============================================================================
class HeadModel(LegendaryModel):
	base_armor = models.TextField(default="660 - 759")

	class Meta:
		abstract = True

@python_2_unicode_compatible
class Helmet(HeadModel):
	affixes = models.ManyToManyField(HelmetAffix, blank=True)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class SpiritStone(HeadModel):
	affixes = models.ManyToManyField(SpiritStoneAffix, blank=True)
	owner = models.TextField(default="Monk")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Spirit Stones'

@python_2_unicode_compatible
class VoodooMask(HeadModel):
	affixes = models.ManyToManyField(VoodooMaskAffix, blank=True)
	owner = models.TextField(default="Witch Doctor")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Voodoo Masks'

@python_2_unicode_compatible
class WizardHat(HeadModel):
	affixes = models.ManyToManyField(WizardHatAffix, blank=True)
	owner = models.TextField(default="Wizard")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Wizard Hats'


@python_2_unicode_compatible
class Shoulders(LegendaryModel):
	affixes = models.ManyToManyField(ShouldersAffix, blank=True)
	base_armor = models.TextField(default="586 - 674")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Shoulders'

@python_2_unicode_compatible
class ChestArmor(LegendaryModel):
	affixes = models.ManyToManyField(ChestArmorAffix, blank=True)
	base_armor = models.TextField(default="660 - 759")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Chest Armor'

@python_2_unicode_compatible
class Cloak(LegendaryModel):
	affixes = models.ManyToManyField(CloakAffix, blank=True)
	base_armor = models.TextField(default="660 - 759")
	owner = models.TextField(default="Demon Hunter")

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Bracers(LegendaryModel):
	affixes = models.ManyToManyField(BracersAffix, blank=True)
	base_armor = models.TextField(default="366 - 421")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Bracers'


@python_2_unicode_compatible
class Gloves(LegendaryModel):
	affixes = models.ManyToManyField(GlovesAffix, blank=True)
	base_armor = models.TextField(default="513 - 590")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Gloves'


@python_2_unicode_compatible
class Belt(LegendaryModel):
	affixes = models.ManyToManyField(BeltAffix, blank=True)
	base_armor = models.TextField(default="440 - 506")

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class MightyBelt(LegendaryModel):
	affixes = models.ManyToManyField(MightyBeltAffix, blank=True)
	base_armor = models.TextField(default="516 - 675")
	owner = models.TextField(default="Barbarian")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Mighty Belts'


@python_2_unicode_compatible
class Pants(LegendaryModel):
	affixes = models.ManyToManyField(PantsAffix, blank=True)
	base_armor = models.TextField(default="660 - 759")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Pants'


@python_2_unicode_compatible
class Boots(LegendaryModel):
	affixes = models.ManyToManyField(BootsAffix, blank=True)
	base_armor = models.TextField(default="513 - 590")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Boots'

#Accessories
#==============================================================================
#==============================================================================
@python_2_unicode_compatible
class Amulet(LegendaryModel):
	affixes = models.ManyToManyField(AmuletAffix, blank=True)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Ring(LegendaryModel):
	affixes = models.ManyToManyField(RingAffix, blank=True)

	def __str__(self):
		return self.name

#Off-Hands
#==============================================================================
#==============================================================================
@python_2_unicode_compatible
class Source(LegendaryModel):
	affixes = models.ManyToManyField(SourceAffix, blank=True)
	owner = models.TextField(default="Wizard")

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Mojo(LegendaryModel):
	affixes = models.ManyToManyField(MojoAffix, blank=True)
	owner = models.TextField(default="Witch Doctor")

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Quiver(LegendaryModel):
	affixes = models.ManyToManyField(QuiverAffix, blank=True)
	owner = models.TextField(default="Demon Hunter")

	def __str__(self):
		return self.name

class ShieldModel(LegendaryModel):
	block_chance = models.TextField(blank=True)
	block_amount = models.TextField(default="17000-19000 -- 21000-25000")
	ancient_block_amount = models.TextField(default="20900-25000 -- 27500-32800")

	class Meta:
		abstract = True

@python_2_unicode_compatible
class CrusaderShield(ShieldModel):
	affixes = models.ManyToManyField(CrusaderShieldAffix, blank=True)
	base_armor = models.TextField(default="1,980 - 2,277")
	owner = models.TextField(default="Crusader")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Crusader Shields'

@python_2_unicode_compatible
class Shield(ShieldModel):
	affixes = models.ManyToManyField(ShieldAffix, blank=True)
	base_armor = models.TextField(default="1,760 - 2,024")
	def __str__(self):
		return self.name

#Weapons
#==============================================================================
#==============================================================================
class WeaponModel(LegendaryModel):
	dps = models.TextField(blank=True)
	damage = models.TextField(blank=True)
	aps = models.TextField(blank=True)

	class Meta:
		abstract = True


# @python_2_unicode_compatible
# class (LegendaryModel):
# 	affixes = models.ManyToManyField(Affix, blank=True)

# 	def __str__(self):
# 		return self.name