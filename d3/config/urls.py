from django.conf.urls import include, url
from django.contrib import admin

# from core.views import IndexView
from itemsets.views import AllSetsView


urlpatterns = [
    url(r'^$', AllSetsView.as_view(), name='index_temp'),
    url(r'^administrator/', include(admin.site.urls)),
    url(r'^legendaries/', include('legendaries.urls')),
    url(r'^sets/', include('itemsets.urls')),
    url(r'^', include('miscitems.urls')),
]