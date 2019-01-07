from __future__ import unicode_literals

from django.db import models
import datetime
from datetime import date
import os

# Create your models here.
class Bdm(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=10)
    alt_contact_no = models.CharField(null=True, blank=True, max_length=10)
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return str(self.name)
    def __str__(self):
        return str(self.name)

class Brand(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return str(self.name)
    def __str__(self):
        return str(self.name)

class City(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return str(self.name)
    def __str__(self):
        return str(self.name)


class Dealer(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    dealer_company = models.CharField(max_length=30)
    dealership_name = models.CharField(max_length=30)
    status = models.CharField(max_length=30, default="Active")
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    sales_outlet = models.BooleanField(default=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    bdm = models.ForeignKey(Bdm, on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.dealership_name)
    def __str__(self):
        return str(self.dealership_name)

class Outlet(models.Model):
    
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=30, blank = True)
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    status = models.CharField(max_length=30, default= "Active")
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    def __unicode__(self):
        return str(self.dealer.dealership_name +", " +self.area)
        
    def __str__(self):
        return str(self.dealer.dealership_name +", "+ self.area)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact_no_1 = models.CharField(null=True, max_length=10)
    contact_no_2 = models.CharField(null=True, max_length=10)
    is_primary_contact = models.BooleanField(default=False)
    type = models.CharField(max_length=20)#for dealer or outlet
    active = models.BooleanField(default=True)
    #image = models.ImageField(null=True, blank=True, upload_to="image/")
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, blank=True, null=True)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE, blank=True, null=True)

#for price module
class DealerPriceFile(models.Model):
    period = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to="./dealerprice")
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

    # def filename(self):
    #     return os.path.basename(self.file.name)
    def __unicode__(self):
        return str(self.period)
    def __str__(self):
        return str(self.period)

#new db model
# automobile
class TransmissionType(models.Model):
    type = models.CharField(max_length=30)
    
    def __unicode__(self):
        return str(self.type)
    def __str__(self):
        return str(self.type)


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    vehicle_type = models.CharField(max_length=30)
    
    def __unicode__(self):
        return str(self.name)
    def __str__(self):
        return str(self.name)


class Variant(models.Model):
    name = models.CharField(max_length=100)
    cc = models.IntegerField(blank=True, null=True)
    seating_capacity = models.IntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=50, blank=True, null=True)
    #transmission_type = models.CharField(max_length=30)
    body = models.CharField(max_length=50, blank=True, null=True)#for dealer or outlet
    category = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    iscorporatediscount = models.BooleanField(default=True)
    #image = models.ImageField(null=True, blank=True, upload_to="image/")
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    transmission_type_id = models.ForeignKey(TransmissionType, on_delete=models.CASCADE, blank=True, null=True)
    
    def __unicode__(self):
        return str(self.name)
    def __str__(self):
        return str(self.model.name + "," + self.name)


class Inventory(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    count = models.IntegerField()
   
    
    def __unicode__(self):
        return str(self.variant.name + self.variant.model.name )
    def __str__(self):
        return str(self.variant.model.name + "," + self.variant.name )


# price
class PriceType(models.Model):
    type = models.CharField(max_length=30)
    
    def __unicode__(self):
        return str(self.type)
    def __str__(self):
        return str(self.type)


class InsuranceType(models.Model):
    type = models.CharField(max_length=30)
    
    def __unicode__(self):
        return str(self.type)
    def __str__(self):
        return str(self.type)

class Rto(models.Model):
    rto_name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return str(self.rto_name)
    def __str__(self):
        return str(self.rto_name)

class DealerDiscount(models.Model):
    discount =  models.DecimalField(max_digits=10, decimal_places=8)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

class DealerOffer(models.Model):
   offers = models.TextField()
   dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
   variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
   city = models.ForeignKey(City, on_delete=models.CASCADE)
   def __unicode__(self):
       return str(self.dealer.dealership_name)
   def __str__(self):
       return str(self.dealer.dealership_name)


class AckodriveKindOffers(models.Model):
    offers = models.TextField(blank=True, null=True)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    def __unicode__(self):
        return str(self.type)
    def __str__(self):
        return str(self.type)


class AckodriveDiscount(models.Model):
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)


class PriceConfig(models.Model):
   # valid_till = models.DateField()
   ex_showroom = models.DecimalField(max_digits=10, decimal_places=2)
   registration_amount = models.DecimalField(max_digits=10, decimal_places=2)
   insurance_premium = models.DecimalField(max_digits=10, decimal_places=2)
   environment_compensation = models.DecimalField(max_digits=10, decimal_places=2)
   octroi = models.DecimalField(max_digits=10, decimal_places=2)
   depot_charges = models.DecimalField(max_digits=10, decimal_places=2)
   rsa_amount = models.DecimalField(max_digits=10, decimal_places=2)
   extended_warranty_amount = models.DecimalField(max_digits=10, decimal_places=2)
   # govt_employee_scheme = models.CharField(max_length=50)#
   # corporate_discount = models.DecimalField(max_digits=10, decimal_places=2)#
   cash_discount = models.DecimalField(max_digits=10, decimal_places=2)
   amc = models.DecimalField(max_digits=10, decimal_places=2)
   basic_accessories = models.DecimalField(max_digits=10, decimal_places=2)
   number_plate = models.DecimalField(max_digits=10, decimal_places=2)
   smart_card = models.DecimalField(max_digits=10, decimal_places=2)
   mcd_charges = models.DecimalField(max_digits=10, decimal_places=2)
   tax_collected_at_source = models.DecimalField(max_digits=10, decimal_places=2)
   road_tax = models.DecimalField(max_digits=10, decimal_places=2)
   other_charges = models.DecimalField(max_digits=10, decimal_places=2)
   # logistic_charges = models.DecimalField(max_digits=10, decimal_places=2)
   # depot_charges = models.DecimalField(max_digits=10, decimal_places=2)
   # nexa_card = models.CharField(max_length=50)
   # honda_connect = models.CharField(max_length=50)
   # honda_genius_access = models.CharField(max_length=50)
   # fast_tag = models.CharField(max_length=50)
   #fk
   # dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
   variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
   city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
   # price_type = models.ForeignKey(PriceType, on_delete=models.CASCADE)
   # insurance_type = models.ForeignKey(InsuranceType, on_delete=models.CASCADE)
   # ackodrive_discount = models.ForeignKey(AckodriveDiscount, on_delete=models.CASCADE)
   # rto = models.ForeignKey(Rto, on_delete=models.CASCADE)

class DealerKindOffer(models.Model):
    BestPrice = models.DecimalField(max_digits=10, decimal_places=2)
    MarketPrice = models.DecimalField(max_digits=10, decimal_places=2)
    price_config = models.ForeignKey(PriceConfig, on_delete=models.CASCADE)

#     class Visit(models.Model):
#         ip = models.CharField(max_length=50 )
#         landing_url = models.CharField(max_length=100)
#         referrer = models.CharField(max_length=100)
#         bounce_url = models.CharField(max_length=100)
#         created_on = models.DateField(_("Date"), default=datetime.now)
#         updated_on = models.DateField(_("Date"), default=datetime.now)
#         tracker = models.CharField(max_length=100)
#         utm_campaign = models.TextField()
#         utm_content = models.TextField()
#         utm_medium = models.TextField()
#         utm_source = models.TextField()
#         utm_term = models.TextField()

class AckodriveQuote(models.Model):
    user_id = models.BigIntegerField()
    variant_id = models.ForeignKey(Variant, on_delete=models.CASCADE)
    dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    outlet_id = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    price_config_id = models.ForeignKey(PriceConfig, on_delete=models.CASCADE)
    corporatediscount_id = models.BigIntegerField()
    pricetype_id = models.ForeignKey(PriceType, on_delete=models.CASCADE)
    insurancetype_id = models.ForeignKey(InsuranceType, on_delete=models.CASCADE)
    dealerdiscount_id = models.ForeignKey(DealerDiscount, on_delete=models.CASCADE)
    ackodrivedicsount_id = models.ForeignKey(AckodriveDiscount, on_delete=models.CASCADE)
    rto_id = models.ForeignKey(Rto, on_delete=models.CASCADE)
    #field =  models.BigIntegerField() json field
    created_on = models.DateField()
    updated_on = models.DateField()

class VariantCorporateDiscount(models.Model):
    discount = models.IntegerField()
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    #need to add corporatediscountID fk



# class VariantCorporateDiscount(models.Model):
#     status = models.CharField(max_length=30 )
#     variant = models.ForeignKey(Variant, on_delete=models.CASCADE)


class Testdrive(models.Model):
    preferred_time_1 =models.TimeField()
    preferred_time_2 =models.TimeField()
    status = models.CharField(max_length=30)
    created_on = models.DateField()
    updated_on = models.DateField()
    quote = models.ForeignKey(AckodriveQuote, on_delete=models.CASCADE)
    #field =  models.BigIntegerField() json field

class Booking(models.Model):
    created_on = models.DateField()
    updated_on = models.DateField()
    quote = models.ForeignKey(AckodriveQuote, on_delete=models.CASCADE)
    testdrive = models.ForeignKey(Testdrive, on_delete=models.CASCADE)
    #field =  models.BigIntegerField() json field




class Payment(models.Model):
    app = models.CharField(max_length=50 )
    okind = models.CharField(max_length=50)
    oid = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=8)
    pg = models.CharField(max_length=100)
    pg_token = models.CharField(max_length=100)
    pg_response = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=30)
    payment_on = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=30)
    order_id = models.CharField(max_length=100)
    user_id = models.IntegerField()

    created_on = models.DateField()
    updated_on = models.DateField()
    #fk user
    quote = models.ForeignKey(AckodriveQuote, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    # form_data = 

class DealerDiscountUpload(models.Model):
    file_name = models.FileField(upload_to="./dealerprice", default="settings.MEDIA_ROOT/dealerprice/anonymous.png")
    model_name = models.CharField(max_length=50)
    variant_name = models.CharField(max_length=50)
    cash_discount = models.DecimalField(max_digits=10, decimal_places=8)
    non_cash_offer = models.DecimalField(max_digits=10, decimal_places=8) 
    dealer_name = models.CharField(max_length=50) 
    # dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=30)

