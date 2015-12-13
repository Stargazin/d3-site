from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^items/legendaries/', include('legendaries.urls')),
    url(r'^items/sets/', include('itemsets.urls')),
    url(r'^items/misc/', include('miscitems.urls')),
    # url(r'^$',),
]