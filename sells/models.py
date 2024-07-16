from django.db import models
from django.forms import model_to_dict


# Create your models here.
class Client(models.Model):
    code = models.CharField(max_length=200, null=True, blank=False)
    name = models.CharField(max_length=200, null=True, blank=False)
    phone = models.CharField(max_length=200, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=225, null=True, blank=False)
    description = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        order_with_respect_to = 'name'

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=225, null=True, blank=False)
    code = models.CharField(max_length=225, unique=True, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created', 'image'])
        return item


    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=225, null=True, blank=False)
    code = models.CharField(max_length=225, unique=True, null=True, blank=False)
    minimunStock = models.IntegerField(null=True, blank=False)
    description = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    cost = models.DecimalField(max_digits=13, decimal_places=0, null=False)
    margin = models.DecimalField(max_digits=13, decimal_places=0, null=False)
    price = models.DecimalField(max_digits=13, decimal_places=0, null=True)
    quantity = models.DecimalField(max_digits=13, decimal_places=0, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        order_with_respect_to = 'description'

    def __str__(self):
        return self.description
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created', 'image'])
        return item
    
    
    
class Proveedor(models.Model):
    name = models.CharField(max_length=225, null=True, blank=False)
    description = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=11, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'
        order_with_respect_to = 'name'

    def __str__(self):
        return self.name
    
class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(Client, on_delete=models.SET_NULL , null=True , related_name='client')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    efectivo = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    tarjeta = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    transferencia = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return str(self.id)
   

class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item

    