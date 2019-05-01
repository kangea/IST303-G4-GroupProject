from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import datetime

class CustomUser(AbstractUser):
    discord = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Brand(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    logo_url = models.URLField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    SKU = models.CharField(max_length=200)
    instock = models.BooleanField()
    picture_url = models.URLField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    restock_date = models.DateTimeField('date restocked')
    original_release_date = models.DateTimeField('original release date')
    watchers = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def was_released_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.original_release_date <= now

class ProductURL(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url
