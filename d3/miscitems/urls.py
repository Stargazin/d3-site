from django.conf.urls import url
from .views import GemView, PotionView, MaterialView, SlotMaterialView, SingleGemView, SinglePotionView, SingleMaterialView

urlpatterns = [
	url(r'^gems/$', GemView.as_view(), name='gems'),
	url(r'^potions/$', PotionView.as_view(), name='potions'),
	url(r'^materials/$', MaterialView.as_view(), name='group-materials'),
	url(r'^materials/(?P<slot_slug>[\w\-]+)/$', SlotMaterialView.as_view(), name='slot-materials'),

	#Single items: gems / potions / materials
	url(r'^single-gem/(?P<name_slug>[\w\-]+)/$', SingleGemView.as_view(), name='single-gem'),
	url(r'^single-potion/(?P<name_slug>[\w\-]+)/$', SinglePotionView.as_view(), name='single-potion'),
	url(r'^single-material/(?P<name_slug>[\w\-]+)/$', SingleMaterialView.as_view(), name='single-material'),
]