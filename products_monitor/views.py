from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Brand, Product

class IndexView(generic.ListView):
    template_name = 'products_monitor/index.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.all().order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['product_list'] = Product.objects .all()
        return context

class ProductView(generic.ListView):
    template_name = 'products_monitor/products.html'
    

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
