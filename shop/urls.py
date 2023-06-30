from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ShopView.as_view(), name='shop'),
    path('producttype/<int:pk>/', views.StockListView.as_view(), name='stocklist'),
    path('orderlist/<int:pk>/', views.OrderListView.as_view(), name='orderlist'),
    path('ordersubmit/<int:pk>', views.OrderSubmitView, name='ordersubmit'),
    path('aboutus/', views.AboutView.as_view(), name='about'),
]

