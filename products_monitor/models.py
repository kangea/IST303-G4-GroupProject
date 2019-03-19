from django.db import models

class Brand(models.Model):
    name = models.CharField()
    url = models.URLField()
    logo_url = models.URLField()

class Product(models.Model):
    name = models.CharField()
    SKU = models.CharField(max_length=200)
    stock_status = models.BinaryField()
    url = models.URLField()
    picture_url = models.URLField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def getSKU(self):
        return self.SKU

    def getImage(self):
        return self.picture_url
