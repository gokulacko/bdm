from django import forms
from .models import Dealer, Bdm, Contact, Outlet    

class BdmForm(forms.ModelForm):
	class Meta:
		model = Bdm
		fields = [
			'name',
			'city',
			'contact_no',
            'alt_contact_no',
            'email'
		]


class DealerForm(forms.ModelForm):
	class Meta:
		model = Dealer
		fields = [
			'brand',
            'dealer_company',
            'dealership_name',
            'status',
            'address',
            'city',
			'sales_outlet',
            'pincode',
            # 'latitude',
            # 'longitude',
            'bdm'
		]

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
			'name',
			'designation',
			'email',
			'contact_no_1',
			'contact_no_2',
			'is_primary_contact',
			'type', 
			'active', 
			#'image', 
			'dealer',
			'outlet'

		]
class ContactFormOutlet(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
			'name',
			'designation',
			'email',
			'contact_no_1',
			'contact_no_2',
			'is_primary_contact',
			'type', 
			'active', 
			#'image', 
			'outlet'

		]

class OutletForm(forms.ModelForm):
	class Meta:
		model = Outlet
		fields = [
			'address',
			'area',
			'city',
			'pincode',
			'status',
			'dealer',
			

		]