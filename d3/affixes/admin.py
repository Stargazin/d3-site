from django.contrib import admin

from .models import Affix


class AffixAdmin(admin.ModelAdmin):
	list_display = ('pk', 'slot', 'category', 'affix', 'is_primary', 'desc')
	list_filter = ('slot', 'category', 'is_primary')


admin.site.register(Affix, AffixAdmin)