from django.conf.urls import include, url
from django.contrib import admin

# from core.views import IndexView
from legendaries.views import AllLegendariesView


urlpatterns = [
    url(r'^$', AllLegendariesView.as_view(), name='index'),
    url(r'^administrator/', include(admin.site.urls)),
    url(r'^legendaries/', include('legendaries.urls')),
    url(r'^sets/', include('itemsets.urls')),
    url(r'^', include('miscitems.urls')),
]