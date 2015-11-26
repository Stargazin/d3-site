from django.contrib import admin

from .models import ItemSet, SetEffect, SetPiece


class ItemSetAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'notes',)
	list_filter = ('owner',)


class SetEffectAdmin(admin.ModelAdmin):
	list_display = ('effect', 'pieces', 'itemSet', 'notes',)
	list_filter = ('itemSet',)


class SetPieceAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'itemSet', 'notes',)
	list_filter = ('itemSet',)


admin.site.register(ItemSet, ItemSetAdmin)
admin.site.register(SetEffect, SetEffectAdmin)
admin.site.register(SetPiece, SetPieceAdmin)