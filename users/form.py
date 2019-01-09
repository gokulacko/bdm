from django import forms
from .models import Profile
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User, Permission



class ProfileForm(forms.ModelForm):
	# CATEGORIES=(
    #     ('Active', 'Active'),
    #     ('Inactive', 'In-Active'),
    #     ('Expired', 'Expired'),
    # )
	# role = forms.ChoiceField(choices=CATEGORIES)
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
		model = Profile
		fields = [
			'first_name',
            'Last_name',
            'city',
            'home_address',
            'phone',
            'email',
			'role',
            'is_active',
            'is_admin',
            'is_staff',
            
            
		]

class MyCustomSignupForm(SignupForm,ProfileForm):

    def save(self, request):

        # Ensure you call the parent classes save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        form = ProfileForm(request.POST)
        
        
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
            
            if form.is_admin:
                user.is_superuser = True
            if form.is_staff:
                user.is_staff = True
            user.save()
           
        

        # Add your own processing here.

        # You must return the original result.
        return user
