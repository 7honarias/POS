from django.urls import path
from . import views

urlpatterns = [
    path('', views.sells_view, name='sells'),
    path('clients', views.clients_view, name='clients'),
    path('add_cliente/', views.add_client_view, name='AddCliente'),
    path('add_cliente/', views.add_client_sell_view, name='AddClienteSell'),
    path('edit_cliente/', views.edit_client_view, name='EditCliente'),
    path('delete_cliente/', views.delete_client_view, name='DeleteCliente'),
    path('products', views.products_view, name='products'),
    path('add_product/', views.add_product_view, name='AddProduct'),
    path('edit_product/', views.edit_product_view, name='EditProduct'),
    path('delete_product/', views.delete_product_view, name='DeleteProduct'),
    path('categories', views.category_view, name='categories'),
    path('add_category/', views.add_category_view, name='AddCategory'),
    path('edit_category/', views.edit_category_view, name='EditCategory'),
    path('delete_category/', views.delete_category_view, name='DeleteCategory'),
    path('add_venta/',views.add_ventas.as_view(), name='AddVenta'),
    path('export/', views.export_pdf_view, name='ExportPDF'),
    path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),
    path('details_sell/<int:sell_id>/', views.details_sell_view, name='Details'),

]
