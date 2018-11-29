from django.shortcuts import render
from .forms import BdmForm, DealerForm, ContactForm
from .models import Dealer, Bdm, Outlet, Contact
# from geopy.geocoders import Nominatim
import googlemaps
from datetime import datetime

# Create your views here.
def index(request):
    
    if request.method == "POST":
        form = BdmForm(request.POST)
        dealerform = DealerForm(request.POST)
        contactform = ContactForm(request.POST)
        dealer = Dealer.objects.all()
        if form.is_valid():
            form.save()
            form = BdmForm()
        if dealerform.is_valid():
            dealerform.save()
            dealerform = DealerForm()
        if contactform.is_valid():
            contactform.save()
            contactform = DealerForm()
    else:
        form = BdmForm()
        dealerform = DealerForm()
        contactform = ContactForm()
        dealer = Dealer.objects.all()
        # gmaps = googlemaps.Client(key='')
        # geolocator = Nominatim(timeout= 10)
        # address = "okilipuram, bangalore"
        # add = "9, 17th A Main Rd, Near Sukh Sagar Restaurant, 5th Block, Koramangala, Bengaluru, Karnataka 560095"
        # location = geolocator.geocode(address)
        # print((location.latitude, location.longitude))
        # geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
        # print(geocode_result)
    return render(request, 'dealer/index.html', {'form':form, 'dealerform':dealerform, 'contactform':contactform, 'dealer':dealer})


def dealer(request, id):
    dealer_info = Dealer.objects.get(id=id)
    dealer_contact = Contact.objects.filter(dealer_id = id)
    outlet_info = Outlet.objects.filter(dealer_id = id)
    outlet_contact = Contact.objects.filter(outlet__dealer__id = id)
    print(outlet_contact)

    return render(request, 'dealer/dealer.html', { 'dealer_info':dealer_info, 'dealer_contact':dealer_contact, 'outlet_info':outlet_info, 'outlet_contact':outlet_contact })



def dealerEdit(request, id):
    if request.method == "POST":
        dealeredit = Dealer.objects.get(id=id)
        dealeredit.brand = request.POST.get('brand')
        dealeredit.dealer_company = request.POST.get('dealer_company')
        dealeredit.dealership_name = request.POST.get('dealership_name')
        dealeredit.status = request.POST.get('status')
        dealeredit.address = request.POST.get('address')
        dealeredit.city = request.POST.get('city')
        dealeredit.pincode = request.POST.get('pincode')
        dealeredit.sales_outlet = request.POST.get('sales_outlet')
        # geolocator = Nominatim(user_agent="ackodrive", timeout= 3)
        # location = geolocator.geocode(request.POST.get('address'))
        # print((location.latitude, location.longitude))
        dealeredit.save()



    dealer_info = Dealer.objects.get(id=id)
    
    return render(request, 'dealer/dealer_edit.html', { 'dealer_info':dealer_info })

def outletEdit(request, id):
    outlet_info = Outlet.objects.get(id=id)
    return render(request, 'dealer/outlet_edit.html', { 'outlet_info':outlet_info })
def contactEdit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form['active'].value())
        # contact = Contact.objects.get(id=id)
        contact.name = request.POST.get('name')
        contact.designation = request.POST.get('designation')
        contact.email = request.POST.get('email')
        contact.contact_no_1 = request.POST.get('contact_no_1')
        contact.contact_no_2 = request.POST.get('contact_no_2')   
        contact.active = form['active'].value()
        contact.save()
    contactform = ContactForm(instance=contact)
    
    return render(request, 'dealer/contact_edit.html', { 'contact':contact, 'contactform':contactform })