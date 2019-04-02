from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django_filters.views import FilterView
from django_filters import rest_framework as filters
from django.utils import timezone
from .filters import ProductFilter

from .models import Brand, Product

class IndexView(generic.ListView):
    template_name = 'products_monitor/index.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.all().order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['product_list_new'] = Product.objects.all().order_by('-original_release_date')[:5]
        context['product_list_restock'] = Product.objects.filter(restock_date__lte=timezone.now()).order_by('-restock_date')[:5]
        return context

class ProductView(FilterView):
    template_name = 'products_monitor/products.html'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    context_object_name = 'product_list'
    ordering_fields = ('price', 'restock_date', 'original_release_date', 'watchers')
    ordering = 'release_date'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products_monitor/product_detail.html'

    def get_queryset(self):
        return Product.objects.all()

class BrandView(generic.ListView):
    template_name = 'products_monitor/brands.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.all().order_by('name')
