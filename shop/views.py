from django.shortcuts import render
from django.urls import reverse_lazy
from inventory.models import ProductType,Product,City,Unit,Stock
from shop.models import Order
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ShopView(ListView):
    model = ProductType
    template_name= 'shop.html'

class StockListView(LoginRequiredMixin, ListView):
    model = Stock
    template_name= 'stocklist.html'

    def get_queryset(self):
        typeid = self.kwargs['pk']

        stocks = Stock.objects.filter(product__type=typeid).values_list('id', flat=True)
        
        return Stock.objects.filter(inventory__city=self.request.user.city,id__in=stocks)
        


  
class OrderListView(LoginRequiredMixin, ListView): 
    model = Order 
    template_name= 'orderlist.html' 

    def get_queryset(self): 
        userid = self.kwargs['pk']
        return Order.objects.filter(user=userid) 

def OrderSubmitView(request, pk): 
    stock = Stock.objects.get(id=pk) 
    if request.method == 'POST': 
        qty = request.POST.get('quantity') 
        if stock.quantity >= int(qty): 
            order = Order.objects.create(user=request.user, product=stock, quantity=qty) 
            order.save() 
            stock.quantity -= int(qty)
            stock.save() 
            return render(request, 'ordersuccess.html') 
        else: 
            return render(request, 'orderfailure.html') 

    else: 
        
        context = { 
                'Stock': stock, 
            } 
        return render(request, 'ordersubmit.html', context) 

class AboutView(TemplateView): 
     template_name="about.html"