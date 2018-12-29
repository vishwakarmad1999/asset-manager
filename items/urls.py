from django.conf.urls import url
from .views import ItemCreateView, ItemView, ItemUpdateView, ItemDeleteView

urlpatterns = [
	url(r'create/$', ItemCreateView.as_view(), name = 'create'),	
	url(r'delete/(?P<pk>\w+)/$', ItemDeleteView.as_view(), name = 'delete'),	
	url(r'update/(?P<pk>\w+)/$', ItemUpdateView.as_view(), name = 'update'),	
	url(r'(?P<pk>\w+)/$', ItemView.as_view(), name = 'detail'),
]