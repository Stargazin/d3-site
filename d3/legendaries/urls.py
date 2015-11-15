from django.conf.urls import url
from .views import PlaygroundView, HelmetView, SpiritStoneView, VoodooMaskView, WizardHatView, ShouldersView, ChestArmorView, CloakView, BracersView, GlovesView, BeltView, MightyBeltView, PantsView, BootsView, AmuletView, RingView, SourceView, CrusaderShieldView, MojoView, QuiverView, ShieldView

urlpatterns = [
	url(r'^playground/$', PlaygroundView.as_view(), name='playground'),
#Armor
#==============================================================================
	# url(r'^legendaries/armor/$', ||View.as_view(), name='armor'),
	# url(r'^legendaries/armor/head/$', ||View.as_view(), name='head'),
	url(r'^legendaries/armor/helmets/$', HelmetView.as_view(), name='helmets'),
	url(r'^legendaries/armor/spiritstones/$', SpiritStoneView.as_view(), name='spiritstones'),
	url(r'^legendaries/armor/voodoomasks/$', VoodooMaskView.as_view(), name='voodoomasks'),
	url(r'^legendaries/armor/wizardhats/$', WizardHatView.as_view(), name='wizardhats'),

	url(r'^legendaries/armor/shoulders/$', ShouldersView.as_view(), name='shoulders'),

	# url(r'^legendaries/armor/torso/$', ||View.as_view(), name='torso'),
	url(r'^legendaries/armor/chestarmor/$', ChestArmorView.as_view(), name='chestarmor'),
	url(r'^legendaries/armor/cloaks/$', CloakView.as_view(), name='cloaks'),

	url(r'^legendaries/armor/bracers/$', BracersView.as_view(), name='bracers'),

	url(r'^legendaries/armor/gloves/$', GlovesView.as_view(), name='gloves'),

	# url(r'^legendaries/armor/waist/$', ||View.as_view(), name='waist'),
	url(r'^legendaries/armor/belts/$', BeltView.as_view(), name='belts'),
	url(r'^legendaries/armor/mightybelts/$', MightyBeltView.as_view(), name='mightybelts'),

	url(r'^legendaries/armor/pants/$', PantsView.as_view(), name='pants'),

	url(r'^legendaries/armor/boots/$', BootsView.as_view(), name='boots'),

#Accessories
#==============================================================================
	# url(r'^legendaries/accessories/$', ||View.as_view(), name='accessories'),
	url(r'^legendaries/accessories/amulets/$', AmuletView.as_view(), name='amulets'),
	url(r'^legendaries/accessories/rings/$', RingView.as_view(), name='rings'),
#Off-Hands
#==============================================================================
	# url(r'^legendaries/offhands/$', ||View.as_view(), name='offhands'),
	url(r'^legendaries/offhands/sources/$', SourceView.as_view(), name='sources'),
	url(r'^legendaries/offhands/crusadershields/$', CrusaderShieldView.as_view(), name='crusadershields'),
	url(r'^legendaries/offhands/mojos/$', MojoView.as_view(), name='mojos'),
	url(r'^legendaries/quivers/$', QuiverView.as_view(), name='quivers'),
	url(r'^legendaries/shields/$', ShieldView.as_view(), name='shields'),


	# url(r'^legendaries//$', View.as_view(), name=''),
]
