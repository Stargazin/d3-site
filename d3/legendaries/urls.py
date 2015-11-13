from django.conf.urls import url
from .views import PlaygroundView, AmuletsView, RingsView

urlpatterns = [
	url(r'^playground/$', PlaygroundView.as_view(), name='playground'),
	url(r'^legendaries/accessories/amulets/$', AmuletsView.as_view(), name='amulets'),
	url(r'^legendaries/accessories/rings/$', RingsView.as_view(), name='rings'),
	# url(r'^legendaries/offhands/sources/$', SourcesView.as_view(), name='sources'),
	# url(r'^legendaries/offhands/crusadershields/$', CrusaderShieldsView.as_view(), name='crusaderShields'),
	##import
	# url(r'^legendaries/accessories/follower/$', FollowerRelicsView.as_view(), name=''),
	
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
]
