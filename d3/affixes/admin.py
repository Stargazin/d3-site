from django.contrib import admin

from .models import AmuletAffix, RingAffix, SourceAffix, CrusaderShieldAffix, MojoAffix, QuiverAffix, ShieldAffix

class AffixAdmin(admin.ModelAdmin):
	list_display = ('affix', 'pk', 'is_primary', 'desc', 'ancient',)
	list_filter = ('is_primary',)

class AmuletAffixAdmin(AffixAdmin):
	pass

class RingAffixAdmin(AffixAdmin):
	pass

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

admin.site.register(AmuletAffix, AmuletAffixAdmin)
admin.site.register(RingAffix, RingAffixAdmin)
admin.site.register(SourceAffix, SourceAffixAdmin)
admin.site.register(CrusaderShieldAffix, CrusaderShieldAffixAdmin)
admin.site.register(MojoAffix, MojoAffixAdmin)
admin.site.register(QuiverAffix, QuiverAffixAdmin)
admin.site.register(ShieldAffix, ShieldAffixAdmin)

# admin.site.register(Affix, AffixAdmin)