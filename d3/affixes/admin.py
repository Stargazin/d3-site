from django.contrib import admin

from .models import AmuletAffix, RingAffix

class AffixAdmin(admin.ModelAdmin):
	list_display = ('affix', 'is_primary', 'desc', 'ancient', 'pk')
	list_filter = ('is_primary',)

class AmuletAffixAdmin(AffixAdmin):
	pass

class RingAffixAdmin(AffixAdmin):
	pass

admin.site.register(AmuletAffix, AmuletAffixAdmin)
admin.site.register(RingAffix, RingAffixAdmin)