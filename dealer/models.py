from django.db import models

# Create your models here.
class Bdm(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    alt_contact_no = models.IntegerField(null = True)
    email = models.CharField(max_length=50)


class Dealer(models.Model):
    brand = models.CharField(max_length=30)
    dealer_company = models.CharField(max_length=30)
    dealership_name = models.CharField()
    bdm = models.ForeignKey(Bdm, on_delete=models.CASCADE)

class Dealercontact(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact_no_1 = models.IntegerField()
    contact_no_2 = models.IntegerField()
    address = models.CharField()
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)


class Dealer(models.Model):
    brand = models.CharField(max_length=30)
    dealer_company = models.CharField(max_length=30)
    dealership_name = models.CharField()
    bdm = models.ForeignKey(Bdm, on_delete=models.CASCADE)

class Outlet(models.Model):
    address = models.CharField()
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

class Outletcontact(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact_no_1 = models.IntegerField()
    contact_no_2 = models.IntegerField()
    address = models.CharField()
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)