from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=25)


class Product(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to = "images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,related_name='address')
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25,null=True)
    street = models.CharField(max_length=35,null=True)
    building = models.CharField(max_length=25,null=True)
    apartment = models.CharField(max_length=25,null=True)
    floor = models.CharField(max_length=25,null=True)
    postal_code = models.IntegerField(null=True, blank=True)
    default_add = models.BooleanField(null=False,default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def make_default(self):
        self.default_add = True


    def __str__(self):
        return self.city



class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=False)
    price = models.IntegerField(default=0,blank=True,null=True)
    quantity = models.IntegerField(default=0,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False, related_name='orders')


    def __str__(self):
        return self.product.name


class Inventory(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name



    






