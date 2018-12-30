from import_export import resources, fields
from .models import DealerDiscountUpload

class DealerDiscountUploadResource(resources.ModelResource):
    class Meta:
        model = DealerDiscountUpload
        skip_unchanged = True
        report_skipped = True
        exclude = ('id')
        import_id_fields = ('model_name',)
        fields = ('model_name', 'variant_name', 'cash_discount', 'non_cash_offer')