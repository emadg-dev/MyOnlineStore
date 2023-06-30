from django.shortcuts import render
from django.urls import reverse_lazy
from inventory.models import ProductType,Product,City,Unit,Stock
from shop.models import Order
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AdminPanelView(LoginRequiredMixin, TemplateView): 
     template_name = 'adminpanel.html'


class AdmOrderListView(ListView,LoginRequiredMixin): 
    model = Order 
    template_name = 'admorderlist.html' 

class AdmOrderUpdateView(UpdateView,LoginRequiredMixin): 
    model = Order 
    template_name = 'admorderupdate.html' 
    fields = ["product",'quantity','status'] 

class AdmOrderDeleteView(DeleteView,LoginRequiredMixin): 
    model = Order 
    template_name = 'admorderdel.html' 
    fields = "__all__" 
    success_url = reverse_lazy('admorderlist') 

class AdmStockListView(ListView,LoginRequiredMixin): 
    model = Stock 
    template_name = 'admstocklist.html' 