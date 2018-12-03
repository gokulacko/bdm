from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
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
            paginator = Paginator(dealer,10)
            page = request.GET.get('page')
            dealer = paginator.get_page(page)
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
    paginator = Paginator(dealer,10)
    page = request.GET.get('page')
    dealer = paginator.get_page(page)
    return render(request, 'dealer/index.html', {'form':form, 'dealerform':dealerform, 'contactform':contactform, 'dealer':dealer})


def dealer(request, id):
    storage = messages.get_messages(request)
    dealer_info = Dealer.objects.get(id=id)
    dealer_contact = Contact.objects.filter(dealer_id = id)
    outlet_info = Outlet.objects.filter(dealer_id = id)
    outlet_contact = Contact.objects.filter(outlet__dealer__id = id)
    

    return render(request, 'dealer/dealer.html', { 'dealer_info':dealer_info, 'dealer_contact':dealer_contact, 'outlet_info':outlet_info, 'outlet_contact':outlet_contact, 'messages':storage })



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
        messages.success(request, 'Dealer edited successfully')



    dealer_info = Dealer.objects.get(id=id)
    
    return render(request, 'dealer/dealer_edit.html', { 'dealer_info':dealer_info })



def addOutlet(request, id):
    # outlet_info = Outlet.objects.get(id=id)
    dealer_id = id
    dealers = Dealer.objects.get(id=dealer_id)
    if request.method == "POST":
        form = OutletForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Outlet added successfully')
            # dealer_id = outlet_info.dealer.id
            return redirect('dealer-view', id=dealer_id)
        else:
            messages.error(request, 'Outlet not added successfully')
    else:
        form = OutletForm(initial={'dealer': dealers})   
    return render(request, 'dealer/add_outlet.html', { 'dealer_id':dealer_id, 'outletform':form})


def outletEdit(request, id):
    outlet_info = Outlet.objects.get(id=id)
    if request.method == "POST":
        form = OutletForm(request.POST, instance=outlet_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Outlet edited successfully')
            dealer_id = outlet_info.dealer.id
            return redirect('dealer-view', id=dealer_id)
        else:
            messages.error(request, 'Outlet not edited successfully')

    form = OutletForm(instance=outlet_info)   
    return render(request, 'dealer/outlet_edit.html', { 'outlet_info':outlet_info, 'form':form })

def contactEdit(request, id):
    storage = messages.get_messages(request)
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        
        contactform = ContactForm(request.POST, instance=contact)
        if contactform.is_valid():
            contactform.save()
            messages.success(request, 'Contact edited successfully')
        else:
            messages.error(request, 'Contact not edited successfully')
            
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
    
    return render(request, 'dealer/contact_edit.html', { 'contact':contact, 'contactform':contactform, 'messages':storage})

def outletContactEdit(request, id):
    storage = messages.get_messages(request)
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        
        contactform = ContactFormOutlet(request.POST, instance=contact)
        if contactform.is_valid():
            contactform.save()
            messages.success(request, 'Contact edited successfully')
        else:
            messages.error(request, 'Contact not edited successfully')
            
        # print(form['active'].value())
        # contact = Contact.objects.get(id=id)
        # contact.name = request.POST.get('name')
        # contact.designation = request.POST.get('designation')
        # contact.email = request.POST.get('email')
        # contact.contact_no_1 = request.POST.get('contact_no_1')
        # contact.contact_no_2 = request.POST.get('contact_no_2')   
        # contact.active = form['active'].value()
        # contact.save()
    contactform = ContactFormOutlet(instance=contact)
    
    return render(request, 'dealer/contact_edit.html', { 'contact':contact, 'contactform':contactform, 'messages':storage})

def addDealerContact(request, id):
    dealer_id = id
    dealers = Dealer.objects.get(id=dealer_id)
    
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            messages.success(request, 'Contact added successfully')
            return redirect('dealer-view', id=dealer_id)
        else:
            messages.error(request, 'Contact not added successfully')
            return redirect('dealer-view', id=dealer_id)
            
    contactform = ContactForm(initial={'dealer': dealers, 'type': "dealer"})
    
    return render(request, 'dealer/add_dealer_contact.html', { 'contactform':contactform, 'dealer_id':dealer_id } )

def deleteOutlet(request,id):
    outlet=Outlet.objects.get(id=id)
    dealer_id = outlet.dealer.id
    Contact.objects.filter(outlet_id=id).delete()
    outlet.delete()
    messages.success(request, 'Outlet deleted successfully')
    return redirect('dealer-view', id=dealer_id)

def deleteDealer(request,id):
    dealer=Dealer.objects.get(id=id)
    outlet=Outlet.objects.filter(dealer_id=id)
    Contact.objects.filter(dealer_id=id).delete()
    for out in outlet:
        Contact.objects.filter(outlet_id=out.id).delete()
   
    outlet.delete()
    dealer.delete()
    messages.success(request, 'Outlet deleted successfully')
    return HttpResponseRedirect('/')
    
    

def deleteContact(request,id):
    contact=Contact.objects.get(id=id)
    
    contact.delete()
    messages.success(request, 'Contact deleted successfully')
    return HttpResponseRedirect('/')

def addOutletContact(request, id):
    outlet_id = id
    outlet=Outlet.objects.get(id=outlet_id)
    dealer_id = outlet.dealer.id
    
    if request.method == "POST":
        contactform = ContactFormOutlet(request.POST)
        if contactform.is_valid():
            contactform.save()
            messages.success(request, 'Contact added successfully')
            return redirect('dealer-view', id=dealer_id)
        else:
            messages.error(request, 'Contact not added successfully')
            
    contactform = ContactFormOutlet(initial={'outlet': outlet, 'type': "outlet"})
    
    return render(request, 'dealer/add_outlet_contact.html', { 'contactform':contactform, 'messages':messages, 'dealer_id':outlet_id } )



