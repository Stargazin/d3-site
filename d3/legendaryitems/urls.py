from django.conf.urls import url
from .views import PlaygroundView, AmuletsView

urlpatterns = [
	url(r'^playground/$', PlaygroundView.as_view(), name='playground'),
	url(r'^legendaries/accessories/amulets/$', AmuletsView.as_view(), name='amulets'),
	##import
	# url(r'^legendaries/accessories/rings/$', RingsView.as_view(), name=''),
	# url(r'^legendaries/accessories/follower/$', FollowerRelicsView.as_view(), name=''),
	
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
	# url(r'^legendaries//$', View.as_view(), name=''),
]
