from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^administrator/', include(admin.site.urls)),
    url(r'^legendaries/', include('legendaries.urls')),
    url(r'^sets/', include('itemsets.urls')),
    url(r'^', include('miscitems.urls')),
]