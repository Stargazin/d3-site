from django.contrib import admin

from .models import AmuletAffix, RingAffix, SourceAffix

class AffixAdmin(admin.ModelAdmin):
	list_display = ('affix', 'is_primary', 'desc', 'ancient', 'pk')
	list_filter = ('is_primary',)

class AmuletAffixAdmin(AffixAdmin):
	pass

class RingAffixAdmin(AffixAdmin):
	pass

class SourceAffixAdmin(AffixAdmin):
	pass

# class AffixAdmin(AffixAdmin):
# 	pass

admin.site.register(AmuletAffix, AmuletAffixAdmin)
admin.site.register(RingAffix, RingAffixAdmin)
admin.site.register(SourceAffix, SourceAffixAdmin)
# admin.site.register(Affix, AffixAdmin)