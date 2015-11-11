from django.conf.urls import url
from . import views

urlpatterns = [
	#general
	url(r'^$', views.index, name='index'),
	url(r'^playground/$', views.playground, name='playground'),
	url(r'^amulets/$', views.amuletsss, name='amuletsss'),
	url(r'^legendaries/accessories/amulets/$', views.amulets, name='amulets')
]
