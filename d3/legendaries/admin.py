from django.contrib import admin

from .models import Amulet, Ring, Source, CrusaderShield, Mojo, Quiver, Shield


class LegendaryAdmin(admin.ModelAdmin):
	list_display = ('name', 'pk', 'unique', 'random_primaries', 'random_secondaries')

class AmuletAdmin(LegendaryAdmin):
	pass

class RingAdmin(LegendaryAdmin):
	pass

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


admin.site.register(Amulet, AmuletAdmin)
admin.site.register(Ring, RingAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(CrusaderShield, CrusaderShieldAdmin)
admin.site.register(Mojo, MojoAdmin)
admin.site.register(Quiver, QuiverAdmin)
admin.site.register(Shield, ShieldAdmin)

# admin.site.register(, Admin)