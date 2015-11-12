from django.contrib import admin

from .models import Amulet, Ring, AmuletAffix, RingAffix


class LegendaryItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'pk', 'unique', 'random_primaries', 'random_secondaries')

class AmuletAdmin(LegendaryItemAdmin):
	pass

class RingAdmin(LegendaryItemAdmin):
	pass


class AffixAdmin(admin.ModelAdmin):
	list_display = ('affix', 'is_primary', 'desc', 'ancient', 'pk')
	list_filter = ('is_primary',)

class AmuletAffixAdmin(AffixAdmin):
	pass

class RingAffixAdmin(AffixAdmin):
	pass


admin.site.register(Amulet, AmuletAdmin)
admin.site.register(AmuletAffix, AmuletAffixAdmin)
admin.site.register(RingAffix, RingAffixAdmin)