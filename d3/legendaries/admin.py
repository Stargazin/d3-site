from django.contrib import admin

from .models import Weapon, Armor, Accessory


class LegendaryItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'slot', 'category', 'notes', 'pk',)
	list_filter = ('slot', 'category', 'owner', 'patch',)

class WeaponAdmin(LegendaryItemAdmin):
	pass

class ArmorAdmin(LegendaryItemAdmin):
	pass

class AccessoryAdmin(LegendaryItemAdmin):
	pass


admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Armor, ArmorAdmin)
admin.site.register(Accessory, AccessoryAdmin)