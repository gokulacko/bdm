from django import forms
from .models import Dealer, Bdm, Contact, Outlet, DealerPriceFile, Inventory, DealerDiscountUpload 

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
	CATEGORIES=(
        ('Active', 'Active'),
        ('Inactive', 'In-Active'),
        ('Expired', 'Expired'),
    )
	status = forms.ChoiceField(choices=CATEGORIES)
	# brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'brand', 'placeholder':'Brand'}))
	# status = forms.CharField(widget=forms.TextInput(attrs={'class': 'status'}))
	# dealer_company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-dealer'}))    
	# dealership_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-dealer'}))
	# address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-dealer'}))
	# city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-dealer'}))
	# sales_outlet = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-dealer'}))
	# pincode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-dealer'}))
	# bdm = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-dealer'}))
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
	# dealer = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
	# type = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
	class Meta:
		model = Contact
		fields = [
			'name',
			'designation',
			'email',
			'is_primary_contact',
			'contact_no_1',
			'contact_no_2',
			'active', 
			'type', 
			#'image', 
			'dealer'
		]


class ContactEditForm(forms.ModelForm):
	# dealer = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
	# type = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
	class Meta:
		model = Contact
		fields = [
			'name',
			'designation',
			'email',
			'is_primary_contact',
			'contact_no_1',
			'contact_no_2',
			'active', 
			'type', 
			#'image', 
			# 'dealer'
		]


class ContactFormOutlet(forms.ModelForm):
	# outlet = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
	# type = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
	class Meta:
		model = Contact
		fields = [
			'name',
			'designation',
			'email',
			'is_primary_contact',
			'contact_no_1',
			'contact_no_2',
			'active', 
			'type', 
			#'image', 
			'outlet'
		]

class ContactFormOutletEdit(forms.ModelForm):
	# outlet = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
	# type = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
	class Meta:
		model = Contact
		fields = [
			'name',
			'designation',
			'email',
			'is_primary_contact',
			'contact_no_1',
			'contact_no_2',
			'active', 
			'type', 
			#'image', 
			# 'outlet'
		]

class OutletForm(forms.ModelForm):
	CATEGORIES=(
        ('Active', 'Active'),
        ('Inactive', 'In-Active'), 
    )
	status = forms.ChoiceField(choices=CATEGORIES)
	# dealer = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
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


class OutletEditForm(forms.ModelForm):
	CATEGORIES=(
        ('Active', 'Active'),
        ('Inactive', 'In-Active'),   
    )
	status = forms.ChoiceField(choices=CATEGORIES)
	# dealer = forms.CharField(
	# 	widget=forms.TextInput(attrs={ 'readonly':'True' })
	# )
	class Meta:
		model = Outlet
		fields = [
			'address',
			'area',
			'city',
			'pincode',
			'status',
			# 'dealer',
		]

class DealerDiscountForm(forms.ModelForm):
	class Meta:
		model = DealerDiscountUpload
		fields = [
			'file_name',
			'dealer_name',
			'city_name' 
		]

class InventoryForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = [
			'variant',
			'count',	
		]
