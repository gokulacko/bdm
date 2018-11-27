from __future__ import unicode_literals

from django.db import models


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



# class Dealer(models.Model):
#     brand = models.CharField(max_length=30)
#     dealer_company = models.CharField(max_length=30)
#     dealership_name = models.CharField()
#     bdm = models.ForeignKey(Bdm, on_delete=models.CASCADE)




