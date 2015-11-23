from django.contrib import admin

from .models import Accessory, Weapon, Armor


class LegendaryAdmin(admin.ModelAdmin):
	list_display = ('name', 'name_slug', 'slot', 'slot_slug', 'category', 'category_slug', 'pk', 'notes')


class ArmorAdmin(LegendaryAdmin):
	pass

class WeaponAdmin(LegendaryAdmin):
	pass

class AccessoryAdmin(LegendaryAdmin):
	pass


admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Armor, ArmorAdmin)