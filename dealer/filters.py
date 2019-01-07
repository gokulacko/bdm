from django import forms
import django_filters
from django_filters.widgets import RangeWidget
import dealer.models as m
from django_select2.forms import ModelSelect2TagWidget

class InventoryFilter(django_filters.FilterSet):
    dealer__brand__name=django_filters.ModelMultipleChoiceFilter(queryset=m.Brand.objects.all(), label='Brand', widget=forms.SelectMultiple(attrs={'class':'brandselect'}))
    variant__model__name=django_filters.ModelMultipleChoiceFilter(queryset=m.Model.objects.all(), label='Model',  widget=forms.SelectMultiple(attrs={'class':'modelselect'}))
    variant__name =django_filters.ModelMultipleChoiceFilter(queryset=m.Variant.objects.all(), label='Variant',  widget=forms.SelectMultiple(attrs={'class':'variantselect'}))
    dealer = django_filters.ModelMultipleChoiceFilter(queryset=m.Dealer.objects.all(), label='Dealer', widget=forms.SelectMultiple(attrs={'class':'dealerselect'}))
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
    city=django_filters.ModelMultipleChoiceFilter(queryset=m.City.objects.all(), label='City', widget=forms.SelectMultiple(attrs={'class':'cityselect'}))
    brand__name=django_filters.ModelMultipleChoiceFilter(queryset=m.Brand.objects.all(), label='Brand',  widget=forms.SelectMultiple(attrs={'class':'brandselect'}))
    dealership_name = django_filters.ModelMultipleChoiceFilter(queryset=m.Dealer.objects.all(), label='Dealer', widget=forms.SelectMultiple(attrs={'class':'dealerselect'}))
    status = django_filters.CharFilter(lookup_expr='icontains', label='Status')

    class Meta:
        model = m.Dealer
        fields = [ 'city', 'brand__name', 'dealership_name','status']

    # def __init__(self, *args, **kwargs):
    #     super(DealerFilter.form, self).__init__(*args, **kwargs)

    #     self.fields['dealership_name'].widget.attrs['class'] = 'dealerselect'

class PriceFilter(django_filters.FilterSet):
    city__name=django_filters.ModelMultipleChoiceFilter(queryset=m.City.objects.all(), label='City', widget=forms.SelectMultiple(attrs={'class':'cityselect'}))
    variant__model__brand__name=django_filters.ModelMultipleChoiceFilter(queryset=m.Brand.objects.all(), label='Brand', widget=forms.SelectMultiple(attrs={'class':'brandselect'}))
    variant__model__name=django_filters.ModelMultipleChoiceFilter(queryset=m.Model.objects.all(), label='Model',  widget=forms.SelectMultiple(attrs={'class':'modelselect'}))
    
    class Meta:
        model = m.PriceConfig
        fields = ['city__name', 'variant__model__name', 'variant__model__brand__name' ]
    

    def __init__(self, *args, **kwargs):
        super(PriceFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()
