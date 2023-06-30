from django.contrib import admin

from .models import City, Inventory,Unit,Product,ProductType, Stock, Supplier

admin.site.register(City)
admin.site.register(Inventory)
admin.site.register(Unit)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Stock)
admin.site.register(Supplier)

