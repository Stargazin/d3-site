from django.contrib import admin

from .models import Helmet, SpiritStone, VoodooMask, WizardHat, Shoulders, ChestArmor, Cloak, Bracers, Gloves, Belt, MightyBelt, Pants, Boots, Amulet, Ring, Source, CrusaderShield, Mojo, Quiver, Shield


class LegendaryAdmin(admin.ModelAdmin):
	list_display = ('name', 'pk', 'unique', 'notes', 'random_primaries', 'random_secondaries')

#Armor
#==============================================================================
class HelmetAdmin(LegendaryAdmin):
	pass

class SpiritStoneAdmin(LegendaryAdmin):
	pass

class VoodooMaskAdmin(LegendaryAdmin):
	pass

class WizardHatAdmin(LegendaryAdmin):
	pass

class ShouldersAdmin(LegendaryAdmin):
	pass

class ChestArmorAdmin(LegendaryAdmin):
	pass

class CloakAdmin(LegendaryAdmin):
	pass

class BracersAdmin(LegendaryAdmin):
	pass

class GlovesAdmin(LegendaryAdmin):
	pass

class BeltAdmin(LegendaryAdmin):
	pass

class MightyBeltAdmin(LegendaryAdmin):
	pass

class PantsAdmin(LegendaryAdmin):
	pass

class BootsAdmin(LegendaryAdmin):
	pass

#Accessories
#==============================================================================
class AmuletAdmin(LegendaryAdmin):
	pass

class RingAdmin(LegendaryAdmin):
	pass

#Off-Hands
#==============================================================================
class SourceAdmin(LegendaryAdmin):
	pass

class CrusaderShieldAdmin(LegendaryAdmin):
	pass

class MojoAdmin(LegendaryAdmin):
	pass

class QuiverAdmin(LegendaryAdmin):
	pass

class ShieldAdmin(LegendaryAdmin):
	pass


# class Admin(LegendaryAdmin):
# 	pass


admin.site.register(Helmet, HelmetAdmin)
admin.site.register(SpiritStone, SpiritStoneAdmin)
admin.site.register(VoodooMask, VoodooMaskAdmin)
admin.site.register(WizardHat, WizardHatAdmin)
admin.site.register(Shoulders, ShouldersAdmin)
admin.site.register(ChestArmor, ChestArmorAdmin)
admin.site.register(Cloak, CloakAdmin)
admin.site.register(Bracers, BracersAdmin)
admin.site.register(Gloves, GlovesAdmin)
admin.site.register(Belt, BeltAdmin)
admin.site.register(MightyBelt, MightyBeltAdmin)
admin.site.register(Pants, PantsAdmin)
admin.site.register(Boots, BootsAdmin)

admin.site.register(Amulet, AmuletAdmin)
admin.site.register(Ring, RingAdmin)

admin.site.register(Source, SourceAdmin)
admin.site.register(CrusaderShield, CrusaderShieldAdmin)
admin.site.register(Mojo, MojoAdmin)
admin.site.register(Quiver, QuiverAdmin)
admin.site.register(Shield, ShieldAdmin)

# admin.site.register(, Admin)