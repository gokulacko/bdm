from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.
class Bdm(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    alt_contact_no = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return str(self.name)
    def __str__(self):
        return str(self.name)


class Dealer(models.Model):
    brand = models.CharField(max_length=30 )
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
    contact_no_1 = models.IntegerField(null=True)
    contact_no_2 = models.IntegerField(null=True)
    is_primary_contact = models.BooleanField(default=False)
    type = models.CharField(max_length=20)#for dealer or outlet
    active = models.BooleanField(default=True)
    #image = models.ImageField(null=True, blank=True, upload_to="image/")
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, blank=True, null=True)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE, blank=True, null=True)

#new db model
# class TransmissionType(models.Model):
#     type = models.CharField(max_length=30)
    
#     def __unicode__(self):
#         return str(self.type)
#     def __str__(self):
#         return str(self.type)


# class Model(models.Model):
#     name = models.CharField(max_length=30)
#     vehicle_type = models.CharField(max_length=30)
    
#     def __unicode__(self):
#         return str(self.name)
#     def __str__(self):
#         return str(self.name)


# class Variant(models.Model):
#     name = models.CharField(max_length=30)
#     cc = models.IntegerField()
#     seating_capacity = models.IntegerField()
#     fuel_type = models.CharField(max_length=30)
#     #transmission_type = models.CharField(max_length=30)
#     body = models.CharField(max_length=30)#for dealer or outlet
#     category = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=False)
#     iscorporatediscount = models.BooleanField(default=True)
#     #image = models.ImageField(null=True, blank=True, upload_to="image/")
#     model = models.ForeignKey(Model, on_delete=models.CASCADE)
#     transmission_type_id = models.ForeignKey(TransmissionType, on_delete=models.CASCADE)
    
#     def __unicode__(self):
#         return str(self.name)
#     def __str__(self):
#         return str(self.name)

# class PriceType(models.Model):
#     type = models.CharField(max_length=30)
    
#     def __unicode__(self):
#         return str(self.type)
#     def __str__(self):
#         return str(self.type)


# class InsuranceType(models.Model):
#     type = models.CharField(max_length=30)
    
#     def __unicode__(self):
#         return str(self.type)
#     def __str__(self):
#         return str(self.type)

# class Rto(models.Model):
#     rto_name = models.CharField(max_length=30)
    
#     def __unicode__(self):
#         return str(self.rto_name)
#     def __str__(self):
#         return str(self.rto_name)

# class DealerDiscount(models.Model):
#     discount = models.IntegerField()
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#     variant = models.ForeignKey(Variant, on_delete=models.CASCADE)


# class AckodriveKindOffers(models.Model):
#     type = models.CharField(max_length=30)
#     variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
#     def __unicode__(self):
#         return str(self.type)
#     def __str__(self):
#         return str(self.type)


# class AckodriveDiscount(models.Model):
#     discount = models.IntegerField()
#     variant = models.ForeignKey(Variant, on_delete=models.CASCADE)


# class PriceConfig(models.Model):
#     valid_till = models.DateField(_("Date"), default=datetime.date.today)
#     ex_showroom = models.DecimalField(max_digits=10, decimal_places=2)
#     registration_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     insurance_premium = models.DecimalField(max_digits=10, decimal_places=2)
#     environment_compensation = models.DecimalField(max_digits=10, decimal_places=2)
#     octroi =
#     depot_charges = models.DecimalField(max_digits=10, decimal_places=2)
#     rsa_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     extended_warranty_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     govt_employee_scheme = 
#     corporate_discount = models.DecimalField(max_digits=10, decimal_places=2)
#     cash_discount = models.DecimalField(max_digits=10, decimal_places=2)
#     amc = models.DecimalField(max_digits=10, decimal_places=2)
#     basic_accessories = models.DecimalField(max_digits=10, decimal_places=2)
#     number_plate = models.DecimalField(max_digits=10, decimal_places=2)
#     smart_card = models.CharField(max_length=50)
#     mcd_charges = models.DecimalField(max_digits=10, decimal_places=2)
#     tax_collected_at_source = models.DecimalField(max_digits=10, decimal_places=2)
#     road_tax = models.DecimalField(max_digits=10, decimal_places=2)
#     other_charges = models.DecimalField(max_digits=10, decimal_places=2)
#     logistic_charges = models.DecimalField(max_digits=10, decimal_places=2)
#     depot_charges = models.DecimalField(max_digits=10, decimal_places=2)
#     nexa_card = 
#     honda_connect = 
#     honda_genius_access = 
#     fast_tag = 
#     #fk
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#     variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
#     price_type = models.ForeignKey(PriceType, on_delete=models.CASCADE)
#     insurance_type = models.ForeignKey(InsuranceType, on_delete=models.CASCADE)
#     ackodrive_discount = models.ForeignKey(AckodriveDiscount, on_delete=models.CASCADE)
#     rto = models.ForeignKey(Rto, on_delete=models.CASCADE)



#     class DealerKindOffer(models.Model):
#         BestPrice = models.DecimalField(max_digits=10, decimal_places=2)
#         MarketPrice = models.DecimalField(max_digits=10, decimal_places=2)
#         price_config = models.ForeignKey(PriceConfig, on_delete=models.CASCADE)



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

#     class AckodriveQuote(models.Model):
#         user_id = models.BigIntegerField()
#         variant_id = models.ForeignKey(Variant, on_delete=models.CASCADE)
#         dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#         outlet_id = models.ForeignKey(Outlet, on_delete=models.CASCADE)
#         price_config_id = models.ForeignKey(PriceConfig, on_delete=models.CASCADE)
#         corporatediscount_id = models.BigIntegerField()
#         pricetype_id = models.ForeignKey(PriceType, on_delete=models.CASCADE)
#         insurancetype_id = models.ForeignKey(InsuranceType, on_delete=models.CASCADE)
#         dealerdiscount_id = models.ForeignKey(DealerDiscount, on_delete=models.CASCADE)
#         ackodrivedicsount_id = models.ForeignKey(AckodriveDiscount, on_delete=models.CASCADE)
#         rto_id = models.ForeignKey(Rto, on_delete=models.CASCADE)
#         #field =  models.BigIntegerField() json field
#         created_on = models.DateField(_("Date"), default=datetime.now)
#         updated_on = models.DateField(_("Date"), default=datetime.now)

#     class VariantCorporateDiscount(models.Model):
#         discount = models.IntegerField()
#         variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
#         #need to add corporatediscountID fk



#     # class VariantCorporateDiscount(models.Model):
#     #     status = models.CharField(max_length=30 )
#     #     variant = models.ForeignKey(Variant, on_delete=models.CASCADE)


#     class Testdrive(models.Model):
#         preferred_time_1 =models.TimeField()
#         preferred_time_2 =models.TimeField()
#         status = models.CharField(max_length=30 )
#         created_on = models.DateField(_("Date"), default=datetime.now)
#         updated_on = models.DateField(_("Date"), default=datetime.now)
#         quote = models.ForeignKey(AckodriveQuote, on_delete=models.CASCADE)
#         testdrive = models.ForeignKey(Testdrive, on_delete=models.CASCADE)
#         #field =  models.BigIntegerField() json field

#     class Booking(models.Model):
#         created_on = models.DateField(_("Date"), default=datetime.now)
#         updated_on = models.DateField(_("Date"), default=datetime.now)
#         quote = models.ForeignKey(AckodriveQuote, on_delete=models.CASCADE)
#         testdrive = models.ForeignKey(Testdrive, on_delete=models.CASCADE)
#         #field =  models.BigIntegerField() json field




# class Payment(models.Model):
#     app = models.CharField(max_length=50 )
#     okind = models.CharField(max_length=50)
#     oid = models.CharField(max_length=30)
#     status = models.CharField(max_length=30)
#     amount = models.DecimalField(max_digits=10, decimal_places=8)
#     pg = models.CharField(max_length=100)
#     pg_token = models.CharField(max_length=100)
#     pg_response = model.CharField(max_length=100)
#     transaction_type = models.CharField(max_length=30)
#     payment_on = models.CharField(max_length=30)
#     payment_method = models.CharField(max_length=30)
#     order_id = models.CharField(max_length=100)
#     status = models.CharField(max_length=30)

#     created_on = models.DateField(_("Date"), default=datetime.now)
#     updated_on = models.DateField(_("Date"), default=datetime.now)
#     #fk user
#     quote = models.ForeignKey(AckodriveQuote, on_delete=models.CASCADE)
#     booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
#     form_data = 

    
