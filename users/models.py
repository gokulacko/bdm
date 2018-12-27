from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    first_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    home_address = models.TextField()
    home_latitude = models.DecimalField(max_digits=10,
        decimal_places=8,
        blank=True,
        null=True,
    )
    home_longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    testdrive_address = models.TextField(blank=True, null=True)
    test_latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    test_longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    

    def __unicode__(self):
        return str(self.first_name)
    def __str__(self):
        return str(self.first_name)