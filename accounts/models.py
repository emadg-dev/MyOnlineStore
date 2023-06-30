from django.db import models
from inventory.models import City,Supplier
from django.urls import reverse
from django.contrib.auth.models import AbstractUser 


class CustomUser(AbstractUser):
    email = models.CharField(max_length=100)
    city = models.ForeignKey(City,
            related_name='user_city',
            default='',
            null=True,
            on_delete=models.CASCADE
            )
    supplier = models.ForeignKey(Supplier,
                related_name='user_supplier',
                default='',
                null=True,
                on_delete=models.CASCADE
            )
    
    def __str__(self): 
        return str(self.email)
    
    def get_absolute_url(self):
        return reverse('shop')
    

