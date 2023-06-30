from django.urls import path 
from .views import *
from inventory.views import StockListView

urlpatterns = [
    path('panel/', AdminPanelView.as_view(), name='adminpanel'),
    path('admorderlist/', AdmOrderListView.as_view(), name='admorderlist'),
    path('admorderupdate/<int:pk>/', AdmOrderUpdateView.as_view(), name='admorderupdate'),
    path('admorderdelete/<int:pk>/', AdmOrderDeleteView.as_view(), name='admorderdelete'),
    path('stocklist/', AdmStockListView.as_view(), name='admstocklist'),
]