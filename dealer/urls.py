from django.conf.urls import  url
from . import views



urlpatterns = [
	url(r'^(?P<id>\d+)/dealer-view/$', views.dealer, name='dealer-view' ),
	url(r'^(?P<id>\d+)/dealer-edit/$', views.dealerEdit, name='dealer-edit' ),
	url(r'^(?P<id>\d+)/outlet-edit/$', views.outletEdit, name='outlet-edit' ),
	
]