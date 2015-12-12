from django.contrib import admin

from .models import Accessory, Weapon, Armor


class LegendaryItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'slot', 'category', 'notes', 'pk')
	list_filter = ('slot', 'category', 'owner')

class ArmorAdmin(LegendaryItemAdmin):
	pass

class WeaponAdmin(LegendaryItemAdmin):
	pass

class AccessoryAdmin(LegendaryItemAdmin):
	pass


admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Armor, ArmorAdmin)