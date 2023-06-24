from django.contrib import admin
from .models import Product,Order,Inventory,User

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(User)