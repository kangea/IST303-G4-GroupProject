from django.urls import path
from .filters import ProductFilter
from django.conf.urls import include, url
from haystack.views import SearchView

from . import views

app_name = 'products_monitor'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('brands', views.BrandView.as_view(), name='brands'),
    url(r'^products/$', views.ProductView.as_view(), name='products'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('<int:product_id>/notify', views.save_product, name="notify"),
    path(r'search/', include('haystack.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.UserProfileView.as_view(), name='userprofile'),
]
