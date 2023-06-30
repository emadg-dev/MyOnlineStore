from django.db import models
from django.urls import reverse

class City(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("citylist")

class Inventory(models.Model):
    city = models.ForeignKey(City,
            related_name='inventory_city',
            on_delete=models.CASCADE,)
    def __str__(self):
        return self.city.name
    
    def get_absolute_url(self):
        return reverse("inventorylist")
    

class Unit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('unitlist')

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('producttypelist')

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type = models.ForeignKey(ProductType,
            related_name='product_type',
            on_delete=models.CASCADE,)
    unit = models.ForeignKey(Unit,
            related_name='product_unit',
            on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('productlist')
    
class Stock(models.Model):
    product = models.ForeignKey(Product,
            related_name='stock_product',
            on_delete=models.CASCADE,)
    inventory = models.ForeignKey(Inventory,
            related_name='stock_inventory',
            on_delete=models.CASCADE,)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.product.name + '(' + str(self.quantity) + ')' + ' : ' + self.inventory.__str__())

    def get_absolute_url(self):
        return reverse('admstocklist')
    

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contactInfo = models.TextField()
    city = models.ForeignKey(City,
            related_name='supplier_city',
            on_delete=models.CASCADE,)
    
    def __str__(self): 
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('supplierlist')





