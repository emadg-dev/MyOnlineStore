from django.urls import path
from . import views

urlpatterns = [
    
    path('unitlist/', views.UnitListView.as_view(), name='unitlist'),
    path('unitadd/', views.UnitAddView.as_view(), name='unitadd'),
    path('unitupdate/<int:pk>/', views.UnitUpdateView.as_view(), name='unitupdate'),
    path('unitdelete/<int:pk>/', views.UnitDeleteView.as_view(), name='unitdelete'),

    path('inventorylist/', views.InventoryListView.as_view(), name='inventorylist'),
    path('inventoryadd/', views.InventoryAddView.as_view(), name='inventoryadd'),
    path('inventoryupdate/<int:pk>/', views.InventoryUpdateView.as_view(), name='inventoryupdate'),
    path('inventorydelete/<int:pk>/', views.InventoryDeleteView.as_view(), name='inventorydelete'),

    path('productlist/', views.ProductListView.as_view(), name='productlist'),
    path('productadd/', views.ProductAddView.as_view(), name='productadd'),
    path('productupdate/<int:pk>/', views.ProductUpdateView.as_view(), name='productupdate'),
    path('productdelete/<int:pk>/', views.ProductDeleteView.as_view(), name='productdelete'),

    path('producttypelist/', views.ProductTypeListView.as_view(), name='producttypelist'),
    path('producttypeadd/', views.ProductTypeAddView.as_view(), name='producttypeadd'),
    path('producttypeupdate/<int:pk>/', views.ProductTypeUpdateView.as_view(), name='producttypeupdate'),
    path('producttypedelete/<int:pk>/', views.ProductTypeDeleteView.as_view(), name='producttypedelete'),

    path('stocklist/', views.StockListView.as_view(), name='stocklist'),
    
    path('stockadd/', views.StockAddView.as_view(), name='stockadd'),
    path('stockupdate/<int:pk>/', views.StockUpdateView.as_view(), name='stockupdate'),
    path('stockdelete/<int:pk>/', views.StockDeleteView.as_view(), name='stockdelete'),

    path('supplierlist/', views.SupplierListView.as_view(), name='supplierlist'),
    path('supplieradd/', views.SupplierAddView.as_view(), name='supplieradd'),
    path('supplierupdate/<int:pk>/', views.SupplierUpdateView.as_view(), name='supplierupdate'),
    path('supplierdelete/<int:pk>/', views.SupplierDeleteView.as_view(), name='supplierdelete'),

    path('citylist/', views.CityListView.as_view(), name='citylist'),
    path('cityadd/', views.CityAddView.as_view(), name='cityadd'),
    path('cityupdate/<int:pk>/', views.CityUpdateView.as_view(), name='cityupdate'),
    path('citydelete/<int:pk>/', views.CityDeleteView.as_view(), name='citydelete'),



    # path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    # path('new_post/', PostCreateView.as_view(), name='post_create'),
]