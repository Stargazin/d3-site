from django.conf.urls import url

from .views import GroupWeaponView, SlotWeaponView, CategoryWeaponView, GroupArmorView, SlotArmorView, CategoryArmorView, GroupAccessoryView, SlotAccessoryView, SingleLegendaryView, AllLegendariesView


urlpatterns = [
	url(r'^weapons/$', GroupWeaponView.as_view(), name='group-weapons'),
	url(r'^weapons/(?P<slot_slug>[\w\-]+)/$', SlotWeaponView.as_view(), name='slot-weapons'),
	url(r'^weapons/(?P<slot_slug>[\w\-]+)/(?P<category_slug>[\w\-]+)/$', CategoryWeaponView.as_view(), name='category-weapons'),

	url(r'^armor/$', GroupArmorView.as_view(), name='group-armor'),
	url(r'^armor/(?P<slot_slug>[\w\-]+)/$', SlotArmorView.as_view(), name='slot-armor'),
	url(r'^armor/(?P<slot_slug>[\w\-]+)/(?P<category_slug>[\w\-]+)/$', CategoryArmorView.as_view(), name='category-armor'),

	url(r'^accessories/$', GroupAccessoryView.as_view(), name='group-accessories'),
	url(r'^accessories/(?P<slot_slug>[\w\-]+)/$', SlotAccessoryView.as_view(), name='slot-accessories'),


	url(r'^single-(?P<group>[\w\-]+)/(?P<name_slug>[\w\-]+)/$', SingleLegendaryView.as_view(), name='single-legendary'),

	url(r'^all/$', AllLegendariesView.as_view(), name='all-legendaries'),
]