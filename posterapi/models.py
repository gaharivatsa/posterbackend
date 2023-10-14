from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=255)
    price = models.FloatField()
    productImage = models.ImageField(upload_to='products/')
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.productname
