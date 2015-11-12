from django.contrib import admin

from .models import Amulet, Ring


class LegendaryAdmin(admin.ModelAdmin):
	list_display = ('name', 'pk', 'unique', 'random_primaries', 'random_secondaries')

class AmuletAdmin(LegendaryAdmin):
	pass

class RingAdmin(LegendaryAdmin):
	pass


admin.site.register(Amulet, AmuletAdmin)
admin.site.register(Ring, RingAdmin)