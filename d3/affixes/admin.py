from django.contrib import admin

from .models import AccessoryAffix, WeaponAffix, ArmorAffix

class AffixAdmin(admin.ModelAdmin):
	list_display = ('pk', 'slot', 'category', 'affix', 'is_primary', 'desc')
	list_filter = ('slot', 'category', 'is_primary')


class WeaponAffixAdmin(AffixAdmin):
	pass

class ArmorAffixAdmin(AffixAdmin):
	pass

class AccessoryAffixAdmin(AffixAdmin):
	pass

admin.site.register(WeaponAffix, WeaponAffixAdmin)
admin.site.register(ArmorAffix, ArmorAffixAdmin)
admin.site.register(AccessoryAffix, AccessoryAffixAdmin)
