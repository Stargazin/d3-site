from django.contrib import admin

from .models import HelmetAffix, SpiritStoneAffix, VoodooMaskAffix, WizardHatAffix, ShouldersAffix, ChestArmorAffix, CloakAffix, BracersAffix, GlovesAffix, BeltAffix, MightyBeltAffix, PantsAffix, BootsAffix, AmuletAffix, RingAffix, SourceAffix, CrusaderShieldAffix, MojoAffix, QuiverAffix, ShieldAffix

class AffixAdmin(admin.ModelAdmin):
	list_display = ('affix', 'pk', 'is_primary', 'desc', 'ancient',)
	list_filter = ('is_primary',)

#Armor
#==============================================================================
class HelmetAffixAdmin(AffixAdmin):
	pass

class SpiritStoneAffixAdmin(AffixAdmin):
	pass

class VoodooMaskAffixAdmin(AffixAdmin):
	pass

class WizardHatAffixAdmin(AffixAdmin):
	pass

class ShouldersAffixAdmin(AffixAdmin):
	pass

class ChestArmorAffixAdmin(AffixAdmin):
	pass

class CloakAffixAdmin(AffixAdmin):
	pass

class BracersAffixAdmin(AffixAdmin):
	pass

class GlovesAffixAdmin(AffixAdmin):
	pass

class BeltAffixAdmin(AffixAdmin):
	pass

class MightyBeltAffixAdmin(AffixAdmin):
	pass

class PantsAffixAdmin(AffixAdmin):
	pass

class BootsAffixAdmin(AffixAdmin):
	pass

#Accessories
#==============================================================================
class AmuletAffixAdmin(AffixAdmin):
	pass

class RingAffixAdmin(AffixAdmin):
	pass

#Off-Hands
#==============================================================================
class SourceAffixAdmin(AffixAdmin):
	pass

class CrusaderShieldAffixAdmin(AffixAdmin):
	pass

class MojoAffixAdmin(AffixAdmin):
	pass

class QuiverAffixAdmin(AffixAdmin):
	pass

class ShieldAffixAdmin(AffixAdmin):
	pass

# class AffixAdmin(AffixAdmin):
# 	pass

admin.site.register(HelmetAffix, HelmetAffixAdmin)
admin.site.register(SpiritStoneAffix, SpiritStoneAffixAdmin)
admin.site.register(VoodooMaskAffix, VoodooMaskAffixAdmin)
admin.site.register(WizardHatAffix, WizardHatAffixAdmin)
admin.site.register(ShouldersAffix, ShouldersAffixAdmin)
admin.site.register(ChestArmorAffix, ChestArmorAffixAdmin)
admin.site.register(CloakAffix, CloakAffixAdmin)
admin.site.register(BracersAffix, BracersAffixAdmin)
admin.site.register(GlovesAffix, GlovesAffixAdmin)
admin.site.register(BeltAffix, BeltAffixAdmin)
admin.site.register(MightyBeltAffix, MightyBeltAffixAdmin)
admin.site.register(PantsAffix, PantsAffixAdmin)
admin.site.register(BootsAffix, BootsAffixAdmin)

admin.site.register(AmuletAffix, AmuletAffixAdmin)
admin.site.register(RingAffix, RingAffixAdmin)

admin.site.register(SourceAffix, SourceAffixAdmin)
admin.site.register(CrusaderShieldAffix, CrusaderShieldAffixAdmin)
admin.site.register(MojoAffix, MojoAffixAdmin)
admin.site.register(QuiverAffix, QuiverAffixAdmin)
admin.site.register(ShieldAffix, ShieldAffixAdmin)

# admin.site.register(Affix, AffixAdmin)