from django.contrib.auth.models import User, Permission
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import Profile

class ProfileResource(resources.ModelResource):
    user = fields.Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(User, 'id'))


    class Meta(object):
        model = Profile
        import_id_fields = ('id',)
        exclude = ('id', )