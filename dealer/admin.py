from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission

from import_export.admin import ImportExportActionModelAdmin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from django import forms
import dealer.models as m
from users.models import Profile
from users.form import ProfileForm

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register your models here.

@admin.register(m.Dealer)
class DealerAdmin(ImportExportActionModelAdmin):
    bdm = fields.Field(
        column_name='bdm',
        attribute='bdm',
        widget=ForeignKeyWidget(m.Bdm, 'id'))
    brand = fields.Field(
        column_name='brand',
        attribute='brand',
        widget=ForeignKeyWidget(m.Brand, 'id'))
    pass
admin.site.register(m.Contact)
admin.site.register(m.Outlet)
@admin.register(m.Bdm)
class BdmAdmin(ImportExportActionModelAdmin):
    
    import_id_fields = ('name', 'city', 'contact_no', 'alt_contact_no', 'email')
    pass

admin.site.register(m.Payment)

admin.site.register(m.Booking)
admin.site.register(m.Testdrive)
admin.site.register(m.VariantCorporateDiscount)
admin.site.register(m.AckodriveQuote)
# admin.site.register(m.DealerKindOffer)
admin.site.register(m.PriceConfig)
admin.site.register(m.AckodriveDiscount)

admin.site.register(m.AckodriveKindOffers)
admin.site.register(m.DealerDiscount)
admin.site.register(m.Rto)
admin.site.register(m.PriceType)
# admin.site.register(m.Variant)
@admin.register(m.Variant)

class VariantAdmin(ImportExportActionModelAdmin):
    list_display = ("name", )
    # list_filter = ("first_name", "phone", "email")
    search_fields = ('name',  )

@admin.register(m.Model)

class ModelAdmin(ImportExportActionModelAdmin):
    list_display = ("name", )
    # list_filter = ("first_name", "phone", "email")
    search_fields = ('name',  )


admin.site.register(m.TransmissionType)
# admin.site.register(m.Brand)
@admin.register(m.Brand)

class BrandAdmin(ImportExportActionModelAdmin):
    list_display = ("name", )
    # list_filter = ("first_name", "phone", "email")
    search_fields = ('name',  )



# admin.site.register(m.DealerPriceFile)
admin.site.register(m.City)

# admin.site.register(m.DealerDiscountUpload)
admin.site.register(m.Inventory)

class BdmAdmin(ImportExportActionModelAdmin):
    pass
