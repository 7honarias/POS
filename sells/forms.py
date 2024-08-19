from django import forms
from sells.models import Client, Product, Category, Pet, Service

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('code', 'name', 'phone')
        labels = {
            'code': 'Cedula',
            'name': 'Nombre',
            'phone': 'Telefono',
        }

class AddPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'age', 'raza', 'recomendation', 'sick')
        labels = {
            'name': 'Nombre',
            'age': 'Edad',
            'raza': 'raza',
            'recomendation': 'recomendacion',
            'sick': 'enfermedad'
        }

class EditarServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('code', 'name', 'status')
        labels = {
            'code': 'code',
            'name': 'Nombre',
            'status': 'status'
        }
    
        widgets = {
            'code': forms.TextInput(attrs={'type': 'text', 'id': 'code_editar'}),
            'name': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'status': forms.TextInput(attrs={'id': 'status_editar'}),
        }

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('code', 'name', 'phone')
        labels = {
            'code': 'Cedula',
            'name': 'Nombre',
            'phone': 'Teléfono',
        }
    
        widgets = {
            'code': forms.TextInput(attrs={'type': 'text', 'id': 'code_editar'}),
            'name': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'phone': forms.TextInput(attrs={'id': 'telefono_editar'}),
        }

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('code', 'name', 'category', 'brand', 'description', 'cost', 'margin', 'quantity', 'price')
        labels = {
            'code': 'code',
            'name': 'name',
            'category': 'category',
            'brand': 'brand',
            'description': 'description',
            'cost': 'cost',
            'margin': 'margin',
            'quantity': 'quantity',
            'price': 'price',

        }
    widgets = {
            'code': forms.TextInput(attrs={'type': 'text', 'id': 'code_editar'}),
            'name': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'category': forms.Select(attrs={'id': 'categoria_editar'}),
            'brand': forms.Select(attrs={'id': 'brand_editar'}),
            'description': forms.TextInput(attrs={'id': 'descripcion_editar'}),
            'cost': forms.NumberInput(attrs={'id': 'costo_editar'}),
            'margin': forms.NumberInput(attrs={'id': 'margin_editar'}),
            'quantity': forms.NumberInput(attrs={'id': 'cantidad_editar'}),
            'price': forms.NumberInput(attrs={'id': 'precio_editar'}),
        }

class EditarProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('price', 'quantity', 'margin','cost')
        labels = {
            'price': 'Precio',
            'quantity': 'Cantidad',
            'margin': 'Margen',
            'cost': 'Costo'
        }
    
        widgets = {
            'price': forms.NumberInput(attrs={'id': 'precio_editar'}),
            'quantity': forms.NumberInput(attrs={'id': 'cantidad_editar'}),
            'margin': forms.NumberInput(attrs={'id': 'margin_editar'}),
            'cost': forms.NumberInput(attrs={'id': 'costo_editar'}),

        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')
        labels = {
            'name': 'name',
            'description': 'description',
        }

class EditarCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')
        labels = {
            'name': 'Nombre',
            'description': 'Description',
        }
    
        widgets = {
            'name': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'description': forms.TextInput(attrs={'id': 'description_editar'}),
        }

