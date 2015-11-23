from django.conf.urls import url
from .views import GemView, PotionView, MaterialView

urlpatterns = [
	url(r'^gems/$', GemView.as_view(), name='gem'),
	url(r'^potions/$', PotionView.as_view(), name='potion'),
	url(r'^materials/$, MaterialView.as_view(), name=material'),
]