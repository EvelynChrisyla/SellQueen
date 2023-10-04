from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(default="MISSING VALUE")
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)

    location = models.CharField(max_length=200)
    owner = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    quantity = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    order_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.order_id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=True, null=True, blank=True)
  