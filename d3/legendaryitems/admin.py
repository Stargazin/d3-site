from django.contrib import admin

from models import Amulet, AmuletAffix


class AmuletAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'pic', 'pk')

class AmuletAffixAdmin(admin.ModelAdmin):
	list_display = ('affix', 'is_primary', 'desc', 'ancient', 'pk')
	list_filter = ('is_primary',)


admin.site.register(Amulet, AmuletAdmin)
admin.site.register(AmuletAffix, AmuletAffixAdmin)