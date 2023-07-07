from django.contrib import admin
from .models import Address, Product,Order,Inventory,User,Wishlist,Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Wishlist)
admin.site.register(Cart)