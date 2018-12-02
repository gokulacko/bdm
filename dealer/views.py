from django.shortcuts import render
from django.contrib import messages
from .forms import BdmForm, DealerForm, ContactForm, OutletForm, ContactFormOutlet
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
        elif dealerform.is_valid():
            dealerform.save()
            dealerform = DealerForm()
        elif contactform.is_valid():
            contactform.save()
            contactform = ContactForm()
        elif request.POST.get('filter'):
            city = request.POST.get('city')
            brand = request.POST.get('brand')
            status = request.POST.get('status')
            if not brand:
                brand = ""
            if not city:
                city = ""
            if not status:
                status = ""
            dealer = Dealer.objects.filter(city__icontains=city, brand__icontains = brand, status__icontains = status)
            form = BdmForm()
            dealerform = DealerForm()
            contactform = ContactForm()
            return render(request, 'dealer/index.html', {'form':form, 'dealerform':dealerform, 'contactform':contactform, 'dealer':dealer})
        
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
    if request.method == "POST":
        form = OutletForm(request.POST, instance=outlet_info)
        if form.is_valid():
            form.save()
            dealer_id = outlet_info.dealer.id
            return dealer(request,dealer_id)

    form = OutletForm(instance=outlet_info)   
    return render(request, 'dealer/outlet_edit.html', { 'outlet_info':outlet_info, 'form':form })

def contactEdit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        contactform = ContactForm(request.POST, instance=contact)
        if contactform.is_valid():
            contactform.save()
            
        # print(form['active'].value())
        # contact = Contact.objects.get(id=id)
        # contact.name = request.POST.get('name')
        # contact.designation = request.POST.get('designation')
        # contact.email = request.POST.get('email')
        # contact.contact_no_1 = request.POST.get('contact_no_1')
        # contact.contact_no_2 = request.POST.get('contact_no_2')   
        # contact.active = form['active'].value()
        # contact.save()
    contactform = ContactForm(instance=contact)
    
    return render(request, 'dealer/contact_edit.html', { 'contact':contact, 'contactform':contactform })

def addDealerContact(request, id):
    dealer_id = id
    messages =""
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            messages = "Contact added successfully"
            
    contactform = ContactForm()
    
    return render(request, 'dealer/add_dealer_contact.html', { 'contactform':contactform, 'messages':messages, 'dealer_id':dealer_id } )

def deleteOutlet(request,id):
    outlet=Outlet.objects.get(id=id)
    dealer_id = outlet.dealer.id
    outlet.delete()
    return dealer(request,dealer_id)

def addOutletContact(request, id):
    outlet_id = id
    outlet=Outlet.objects.get(id=outlet_id)
    dealer_id = outlet.dealer.id
    messages =""
    if request.method == "POST":
        contactform = ContactFormOutlet(request.POST)
        if contactform.is_valid():
            contactform.save()
            messages = "Contact added successfully"
            return dealer(request, dealer_id)
            
    contactform = ContactFormOutlet()
    
    return render(request, 'dealer/add_outlet_contact.html', { 'contactform':contactform, 'messages':messages, 'dealer_id':outlet_id } )



