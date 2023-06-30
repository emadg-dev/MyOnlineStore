from django.db import models
from inventory.models import Stock
from django.urls import reverse
from accounts.models import CustomUser   
    
class Order(models.Model):
    user = models.ForeignKey(CustomUser,
            on_delete=models.CASCADE)
    product = models.ForeignKey(Stock, 
            on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=0)
    
    Submitted = 'submitted'
    ReadyToSend = 'ready to send'
    Status_Options = [(Submitted, 'submitted'),
        (ReadyToSend, 'ready to send'),]
    
    status = models.CharField(max_length=50, choices=Status_Options, default=Submitted)
  
    def get_absolute_url(self): 
        return reverse('admorderlist')
    
    def __str__(self):
        return str (self.user.user + ": " + self.product, self.quantity)
    
    def GetCost(self):
        return self.product.product.price

