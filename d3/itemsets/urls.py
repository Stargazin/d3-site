from django.conf.urls import url

from .views import AllSetsView, SingleSetView


urlpatterns = [
	url(r'^$', AllSetsView.as_view(), name='all-sets'),
	url(r'^(?P<owner_slug>[\w\-]+)/(?P<name_slug>[\w\-]+)/$', SingleSetView.as_view(), name='single-set')
]