from django.urls import path

from . import views

app_name = 'products_monitor'
urlpatterns = [
    path('', views.index, name='index')
]
