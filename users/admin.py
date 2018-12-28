from django.contrib import admin
import csv
from django.http import HttpResponse

# Register your models here.
import users.models as m



class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(m.Profile)
class ProfileAdmin(admin.ModelAdmin, ExportCsvMixin):
    # list_display = ("name", "is_immortal", "category", "origin", "is_very_benevolent")
    # list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)
    actions = ["export_as_csv"]