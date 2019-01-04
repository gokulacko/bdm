
import django_filters
from django_filters.widgets import RangeWidget
import dealer.models as m

class InventoryFilter(django_filters.FilterSet):
    dealer__brand__name=django_filters.ModelMultipleChoiceFilter(queryset=m.Brand.objects.all(), label='Brand')
    variant__model__name=django_filters.ModelMultipleChoiceFilter(queryset=m.Model.objects.all(), label='Model')
    variant__name =django_filters.ModelMultipleChoiceFilter(queryset=m.Variant.objects.all(), label='Variant')
   
    class Meta:
        model = m.Inventory
        fields = [ 'dealer', 'dealer__brand__name', 'variant__model__name','variant__name']
        # field_labels={
        # 'dealer__brand__name': 'Brand',
        # }
        # fields = {'dealer': ['icontains', ],
        # 'dealer__brand__name': ['icontains', ], 
        # 'variant__model__name': ['icontains', ], 
        # 'variant__name': ['icontains', ], 
        # }

class DealerFilter(django_filters.FilterSet):
    city=django_filters.ModelMultipleChoiceFilter(queryset=m.City.objects.all(), label='City')
    brand__name=django_filters.ModelMultipleChoiceFilter(queryset=m.Brand.objects.all(), label='Brand')
    dealership_name = django_filters.ModelMultipleChoiceFilter(queryset=m.Dealer.objects.all(), label='Dealer')
    status = django_filters.CharFilter(lookup_expr='icontains', label='Status')

    class Meta:
        model = m.Dealer
        fields = [ 'city', 'brand__name', 'dealership_name','status']
