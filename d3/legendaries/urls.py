from django.conf.urls import url
from .views import PlaygroundView, LegendaryView, SlotView, CategoryView


urlpatterns = [
	url(r'^/playground/$', PlaygroundView.as_view(), name='playground'),
	url(r'^/(?P<model>[\w\-]+)/$', LegendaryView.as_view(), name='legendary'),
	url(r'^/(?P<model>[\w\-]+)/(?P<slot_slug>[\w\-]+)/$', SlotView.as_view(), name='slot'),
	url(r'^/(?P<model>[\w\-]+)/(?P<slot_slug>[\w\-]+)/(?P<category_slug>[\w\-]+)/$', CategoryView.as_view(), name='category'),
	# url(r'^/(?P<name_slug>[\w\-]+)/$', SingleLegendaryView.as_view(), name='single-legendary'),
]