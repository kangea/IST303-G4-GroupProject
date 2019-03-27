from django.urls import path

from . import views

app_name = 'products_monitor'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('brands', views.BrandView.as_view(), name='brands'),
    path('products', views.ProductView.as_view(), name='products'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail')
]
