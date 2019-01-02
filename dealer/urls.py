from django.conf.urls import  url
from . import views

app_name = "dealer"

urlpatterns = [
	url(r'^dashboard$', views.index, name='index' ),
	url(r'^price/$', views.dealerPrice, name='price'),
	url(r'^add-dealer/$', views.addDealer, name='add-dealer' ),
	url(r'^inventory/$', views.inventory, name='inventory' ),
	url(r'^discount/$', views.discount, name='discount' ),
	url(r'^(?P<id>\d+)/dealer-view/$', views.dealer, name='dealer-view' ),
	url(r'^(?P<id>\d+)/dealer-price-view/$', views.dealerPrice, name='dealer-price-view' ),
	url(r'^(?P<id>\d+)/add-outlet/$', views.addOutlet, name='add-outlet' ),
	url(r'^(?P<id>\d+)/dealer-edit/$', views.dealerEdit, name='dealer-edit' ),
	url(r'^(?P<id>\d+)/outlet-edit/$', views.outletEdit, name='outlet-edit' ),
	url(r'^(?P<id>\d+)/contact-edit/$', views.contactEdit, name='contact-edit' ),
	url(r'^(?P<id>\d+)/inventory-edit/$', views.inventoryEdit, name='inventory-edit' ),
	url(r'^(?P<id>\d+)/edit-outlet-contact/$', views.outletContactEdit, name='edit-outlet-contact' ),
	url(r'^(?P<id>\d+)/add-dealer-contact/$', views.addDealerContact, name='add-dealer-contact' ),
	url(r'^(?P<id>\d+)/add-outlet-contact/$', views.addOutletContact, name='add-outlet-contact' ),
	url(r'^(?P<id>\d+)/outlet-delete/$', views.deleteOutlet, name='outlet-delete' ),
	url(r'^(?P<id>\d+)/dealer-delete/$', views.deleteDealer, name='dealer-delete' ),
	url(r'^(?P<id>\d+)/contact-delete/$', views.deleteContact, name='contact-delete' ),
	url(r'^(?P<id>\d+)/dealer-price-download/$', views.dealerPriceFileDownload, name='dealer-price-download'),
	
	url(r'^(?P<id>\d+)/inventory-delete/$', views.deleteInventory, name='inventory-delete' ),
]