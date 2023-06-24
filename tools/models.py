from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=25)
    city = models.CharField(max_length=15,null=True)
    zip = models.IntegerField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to = "images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=False)
    price = models.IntegerField(default=0,blank=True,null=True)
    quantity = models.IntegerField(default=0,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class Inventory(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)

    # def __str__(self):
    #     return self.title





