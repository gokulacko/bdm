from django.contrib import admin

# Register your models here.
import dealer.models as m

# class DealerPriceFileAdmin(admin.ModelAdmin):
#     list_display = ('file', 'dealer', 'period')
#     model = m.DealerPriceFile

admin.site.register(m.Dealer)
admin.site.register(m.Contact)
admin.site.register(m.Outlet)
admin.site.register(m.Bdm)
admin.site.register(m.Payment)

admin.site.register(m.Booking)
admin.site.register(m.Testdrive)
admin.site.register(m.VariantCorporateDiscount)
admin.site.register(m.AckodriveQuote)
admin.site.register(m.DealerKindOffer)
admin.site.register(m.PriceConfig)
admin.site.register(m.AckodriveDiscount)

admin.site.register(m.AckodriveKindOffers)
admin.site.register(m.DealerDiscount)
admin.site.register(m.Rto)
admin.site.register(m.PriceType)
admin.site.register(m.Variant)
admin.site.register(m.Model)
admin.site.register(m.TransmissionType)
admin.site.register(m.Brand)
admin.site.register(m.DealerPriceFile)
admin.site.register(m.City)

admin.site.register(m.DealerDiscountUpload)
