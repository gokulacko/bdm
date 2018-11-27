from django.contrib import admin

# Register your models here.

from .models import Dealer, Contact, Outlet, Bdm

admin.site.register(Dealer)
admin.site.register(Contact)
admin.site.register(Outlet)
admin.site.register(Bdm)