from django.contrib import admin

from .models import Amulet, Ring, Source


class LegendaryAdmin(admin.ModelAdmin):
	list_display = ('name', 'pk', 'unique', 'random_primaries', 'random_secondaries')

class AmuletAdmin(LegendaryAdmin):
	pass

class RingAdmin(LegendaryAdmin):
	pass

class SourceAdmin(LegendaryAdmin):
	pass


# class Admin(LegendaryAdmin):
# 	pass


admin.site.register(Amulet, AmuletAdmin)
admin.site.register(Ring, RingAdmin)
admin.site.register(Source, SourceAdmin)
# admin.site.register(, Admin)