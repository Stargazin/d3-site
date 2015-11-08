from django.contrib import admin

from models import Material


class MaterialAdmin(admin.ModelAdmin):
	list_display = ('name', 'rarity', 'desc', 'id',)
	list_filter = ('rarity',)

admin.site.register(Material, MaterialAdmin)