from django.contrib import admin

from models import Gem, Potion, Material


class GemAdmin(admin.ModelAdmin):
	list_display = ('name', 'unique', 'rank_unique')

class PotionAdmin(admin.ModelAdmin):
	list_display = ('name', 'unique')

class MaterialAdmin(admin.ModelAdmin):
	list_display = ('name', 'pk', 'rarity', 'unique', 'id',)
	list_filter = ('rarity',)


admin.site.register(Gem, GemAdmin)
admin.site.register(Potion, PotionAdmin)
admin.site.register(Material, MaterialAdmin)