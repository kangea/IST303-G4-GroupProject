from .models import Product
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    price = filters.RangeFilter(lookup_expr='range')
    instock = filters.BooleanFilter(field_name='instock')
    restock_date = filters.DateRangeFilter(field_name='restock_date')
    restock_date__range = filters.DateFromToRangeFilter(field_name='restock_date')
    release_date = filters.DateRangeFilter(field_name='original_release_date')
    release_date__range = filters.DateFromToRangeFilter(field_name='original_release_date')

    o = filters.OrderingFilter(
        fields=(
            ('price', 'price'),
            ('restock_date', 'restock_date'),
            ('original_release_date', 'original_release_date'),
            ('watchers', 'watchers'),
        ),

        field_labels={
            'restock_date': 'Restock Date',
            'original_release_date': 'Release Date',
            'watchers': 'Popularity',
        }

    )

    class Meta:
        model = Product
        fields = [ 'brand', 'instock', ]
