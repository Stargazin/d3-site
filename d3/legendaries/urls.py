from django.conf.urls import url
from .views import PlaygroundView, AmuletView, RingView, SourceView, CrusaderShieldView, MojoView, QuiverView, ShieldView

urlpatterns = [
	url(r'^playground/$', PlaygroundView.as_view(), name='playground'),
#Accessories===================================================================
	url(r'^legendaries/accessories/amulets/$', AmuletView.as_view(), name='amulets'),
	url(r'^legendaries/accessories/rings/$', RingView.as_view(), name='rings'),
#Off-Hands=====================================================================
	url(r'^legendaries/offhands/sources/$', SourceView.as_view(), name='sources'),
	url(r'^legendaries/offhands/crusadershields/$', CrusaderShieldView.as_view(), name='crusadershields'),
	url(r'^legendaries/offhands/mojos/$', MojoView.as_view(), name='mojos'),
	url(r'^legendaries/quivers/$', QuiverView.as_view(), name='quivers'),
	url(r'^legendaries/shields/$', ShieldView.as_view(), name='shields'),

	##import
	# url(r'^legendaries//$', View.as_view(), name=''),
]
