from django.contrib import admin
import xlwt
import csv
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from import_export.admin import ImportExportActionModelAdmin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .resources import ProfileResource

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

    export_as_csv.short_description = "Export Selected as Csv"

    def export_as_xls(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        print(field_names)
        for col_num in range(len(field_names)):
            ws.write(row_num, col_num, field_names[col_num], font_style)
  
        
        for row in queryset:
            row_num += 1
            ws.write(row_num, 0, row.user.username, font_style)
            ws.write(row_num, 1, row.first_name, font_style)
            ws.write(row_num, 2, row.Last_name, font_style)
            ws.write(row_num, 3, row.city, font_style)
            ws.write(row_num, 4, row.home_address, font_style)
            ws.write(row_num, 5, row.home_latitude, font_style)
            ws.write(row_num, 6, row.home_longitude, font_style)
            ws.write(row_num, 7, row.testdrive_address, font_style)
            ws.write(row_num, 8, row.test_latitude, font_style)
            ws.write(row_num, 9, row.test_longitude, font_style)
            ws.write(row_num, 10, row.phone, font_style)
            ws.write(row_num, 11, row.email, font_style)
            ws.write(row_num, 12, row.role, font_style)
            ws.write(row_num, 13, row.is_active, font_style)
            ws.write(row_num, 14, row.is_admin, font_style)
            ws.write(row_num, 15, row.is_staff, font_style)

        wb.save(response)
        return response

    export_as_xls.short_description = "Export Selected as Excel"

#admin.ModelAdmin, ExportCsvMixin,
@admin.register(m.Profile)

class ProfileAdmin(ImportExportActionModelAdmin):
    list_display = ("first_name", "phone", "email", "role","is_active","is_staff","is_admin")
    # list_filter = ("first_name", "phone", "email")
    search_fields = ('first_name', 'phone', 'email', 'role' )
    user = fields.Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(m.User, 'username'))
    
    
    
    pass
    # actions = ["export_as_csv", "export_as_xls"]
# admin.site.register(m.Profile, ProfileAdmin)