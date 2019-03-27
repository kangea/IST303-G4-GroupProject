from django.db import models
import datetime

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
    stock_status = models.BinaryField()
    url = models.URLField()
    picture_url = models.URLField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    restock_date = models.DateTimeField('date restocked')
    new_product = models.BinaryField()

    def __str__(self):
        return self.name

    def getSKU(self):
        return self.SKU

    def getImage(self):
        return self.picture_url

    def was_restocked_recently(self):
        now = timezone.now()
        # check with Quan if this is a good time range
        return now-datetime.timedelta(hour=8) <= self.restock_date <= now
