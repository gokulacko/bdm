from django.contrib import admin

# Register your models here.

from .models import Dealer, Contact, Outlet, Bdm, Payment, Booking, VariantCorporateDiscount, AckodriveQuote, DealerKindOffer, Rto
from .models import PriceConfig, AckodriveKindOffers, DealerDiscount, InsuranceType, Variant, PriceType, Model, TransmissionType, Testdrive, AckodriveDiscount
admin.site.register(Dealer)
admin.site.register(Contact)
admin.site.register(Outlet)
admin.site.register(Bdm)
admin.site.register(Payment)

admin.site.register(Booking)
admin.site.register(Testdrive)
admin.site.register(VariantCorporateDiscount)
admin.site.register(AckodriveQuote)
admin.site.register(DealerKindOffer)
admin.site.register(PriceConfig)
admin.site.register(AckodriveDiscount)

admin.site.register(AckodriveKindOffers)
admin.site.register(DealerDiscount)
admin.site.register(Rto)
admin.site.register(PriceType)
admin.site.register(Variant)
admin.site.register(Model)
admin.site.register(TransmissionType)
