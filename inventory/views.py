from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from .models import Unit, Product, ProductType, City, Inventory, Stock, Supplier

from django.contrib.auth.mixins import LoginRequiredMixin

class InventoryListView(ListView,LoginRequiredMixin): 
    model = Inventory 
    template_name = 'inventorylist.html' 

class InventoryAddView(CreateView,LoginRequiredMixin): 
    model = Inventory 
    template_name = 'inventoryadd.html' 
    fields = "__all__" 

class InventoryUpdateView(UpdateView,LoginRequiredMixin): 
    model = Inventory 
    template_name = 'inventoryupdate.html' 
    fields = "__all__" 

class InventoryDeleteView(DeleteView,LoginRequiredMixin): 
    model = Inventory 
    template_name = 'inventorydel.html' 
    fields = "__all__" 
    success_url = reverse_lazy('inventorylist') 



class CityListView(ListView,LoginRequiredMixin): 
    model = City 
    template_name = 'citylist.html' 

class CityAddView(CreateView, LoginRequiredMixin): 
    model = City 
    template_name = 'cityadd.html' 
    fields = '__all__'

class CityUpdateView(UpdateView,LoginRequiredMixin): 
    model = City 
    template_name = 'cityUpdate.html' 
    fields = ['name'] 

class CityDeleteView(DeleteView,LoginRequiredMixin): 
    model = City 
    template_name = 'citydel.html' 
    fields = ['name'] 
    success_url = reverse_lazy('citylist') 


class UnitListView(ListView, LoginRequiredMixin):
    template_name='unitlist.html'
    model = Unit
    context_object_name = 'unitlist'

class UnitAddView(CreateView, LoginRequiredMixin): 
    model = Unit 
    template_name = 'unitadd.html' 
    fields = '__all__'

class UnitUpdateView(UpdateView,LoginRequiredMixin): 
    model = Unit 
    template_name = 'unitUpdate.html' 
    fields = ['name'] 

class UnitDeleteView(DeleteView,LoginRequiredMixin): 
    model = Unit 
    template_name = 'unitdel.html' 
    fields = ['name'] 
    success_url = reverse_lazy('unitlist') 


class ProductTypeListView(ListView,LoginRequiredMixin): 
    model = ProductType
    template_name = 'producttypelist.html' 

class ProductTypeAddView(CreateView,LoginRequiredMixin): 
    model = ProductType
    template_name = 'producttypeadd.html' 
    fields = ['name'] 

class ProductTypeUpdateView(UpdateView,LoginRequiredMixin): 
    model = ProductType
    template_name = 'producttypeupdate.html' 
    fields = ['name'] 

class ProductTypeDeleteView(DeleteView,LoginRequiredMixin): 
    model = ProductType
    template_name = 'producttypedel.html' 
    fields = '__all__'
    success_url = reverse_lazy('producttypelist') 



class ProductListView(ListView,LoginRequiredMixin): 
    model = Product 
    template_name = 'productlist.html' 

class ProductAddView(CreateView,LoginRequiredMixin): 
    model = Product 
    template_name = 'productadd.html' 
    fields = '__all__'

class ProductUpdateView(UpdateView,LoginRequiredMixin): 
    model = Product 
    template_name = 'productUpdate.html' 
    fields = ['name','price', 'type'] 

class ProductDeleteView(DeleteView,LoginRequiredMixin): 
    model = Product 
    template_name = 'productdel.html' 
    fields = '__all__' 
    success_url = reverse_lazy('productlist') 




class SupplierListView(ListView,LoginRequiredMixin): 
    model = Supplier 
    template_name = 'supplierlist.html' 

class SupplierAddView(CreateView,LoginRequiredMixin): 
    model = Supplier 
    template_name = 'supplieradd.html' 
    fields = "__all__" 

class SupplierUpdateView(UpdateView,LoginRequiredMixin): 
    model = Supplier 
    template_name = 'supplierupdate.html' 
    fields = "__all__" 

class SupplierDeleteView(DeleteView,LoginRequiredMixin): 
    model = Supplier 
    template_name = 'supplierdel.html' 
    fields = "__all__" 
    success_url = reverse_lazy('supplierlist') 





class StockListView(ListView,LoginRequiredMixin): 
    model = Stock 
    template_name = 'stocklist.html' 

class StockAddView(CreateView,LoginRequiredMixin): 
    model = Stock
    template_name = 'stockadd.html' 
    fields = "__all__" 

class StockUpdateView(UpdateView,LoginRequiredMixin): 
    model = Stock 
    template_name = 'stockupdate.html' 
    fields = "__all__" 

class StockDeleteView(DeleteView,LoginRequiredMixin): 
    model = Stock 
    template_name = 'stockdel.html' 
    fields = "__all__" 
    success_url = reverse_lazy('admstocklist')