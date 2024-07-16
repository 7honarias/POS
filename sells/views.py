import json
from django.shortcuts import render, redirect
from .models import Client, Product, Category, Egreso, ProductosEgreso
from .forms import AddClientForm, EditarClienteForm, AddProductForm, AddCategoryForm, EditarCategoryForm, EditarProductForm
from django.contrib import messages
from django.utils.dateparse import parse_date
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
#from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template
#from weasyprint import HTML, CSS
from django.conf import settings
import os
from datetime import date


# Create your views here.
def sells_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    sells = Egreso.objects.all()
    
    if start_date and end_date:
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
        sells = sells.filter(fecha_pedido__range=[start_date, end_date])
    context = {
        'sells': sells
    }
    return render(request, 'sells.html', context)

def clients_view(request):
    clients = Client.objects.all()
    form_personal = AddClientForm()
    form_editar = EditarClienteForm()
    context = {
        'clients': clients,
        'form_personal': form_personal,
        'form_editar': form_editar,
    }
    return render(request, 'clients.html', context)


def add_client_view(request):
    print("guardar cliente")
    if request.POST:
        form = AddClientForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, "Error al guardar")
                return redirect('clients')
    return redirect('clients')


def edit_client_view(request):
    client = Client.objects.get(pk=request.POST.get('id_personal_editar'))
    form = EditarClienteForm(request.POST, request.FILES, instance=client)
    if form.is_valid():
        form.save()
    return redirect('clients')


def delete_client_view(request):
    if request.POST:
        client = Client.objects.get(pk=request.POST.get('id_personal_eliminar'))
        client.delete()
    return redirect('clients')

def products_view(request):
    products = Product.objects.all()
    form_product = AddProductForm()
    form_editar = EditarProductForm()
    context = {
        'products': products,
        'form_product': form_product,
        'form_editar': form_editar,
    }
    return render(request, 'products.html', context)


def edit_product_view(request):
    product = Product.objects.get(pk=request.POST.get('id_producto_editar'))
    form = EditarProductForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
        form.save()
    return redirect('products')

def add_product_view(request):
    print("guardar product")
    if request.POST:
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, "Error al guardar")
                return redirect('products')
    return redirect('products')


def category_view(request):
    categories = Category.objects.all()
    form_category = AddCategoryForm()
    form_edit = EditarCategoryForm()
    context = {
        'categories': categories,
        'form_category': form_category,
        'form_editar': form_edit,
    }
    return render(request, 'categories.html', context)

def details_sell_view(request, egreso_id):
    products = ProductosEgreso.objects.filter(egreso__id=egreso_id)
    egreso = Egreso.objects.get(pk=egreso_id)
    print(egreso.__dict__)
    context = {
        'products': products,
        'egreso': egreso,
    }
    return render(request, 'details_sell.html', context)

def add_category_view(request):
    print("guardar categoria")
    if request.POST:
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, "Error al guardar")
                return redirect('categories')
    return redirect('categories')

def delete_category_view(request):
    if request.POST:
        category = Category.objects.get(pk=request.POST.get('id_personal_eliminar'))
        category.delete()
    return redirect('categories')


def edit_category_view(request):
    category = Category.objects.get(pk=request.POST.get('id_personal_editar'))
    form = EditarCategoryForm(request.POST, request.FILES, instance=category)
    if form.is_valid():
        form.save()
    return redirect('categories')

class add_ventas(ListView):
    template_name = 'add_sells.html'
    model = Egreso

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Product.objects.filter(code__icontains=request.POST["term"])[0:10]:
                    print(i)
                    item = i.toJSON()
                    item['value'] = i.code
                    data.append(item)
            elif action == 'save':

                fecha = request.POST['fecha']
                id_cliente = request.POST['id_cliente']
                products = json.loads(request.POST['verts'])
                comentarios = request.POST['comentarios']
                efectivo = request.POST['efectivo']
                tarjeta = request.POST['tarjeta']
                transferencia = request.POST['transferencia']
                total = request.POST['total']
                ticket = True
                desglosar = False

                client = Client.objects.get(id=id_cliente)
                egreso = Egreso(
                    fecha_pedido=fecha,
                    cliente=client,
                    total=total,
                    efectivo=efectivo,
                    tarjeta=tarjeta,
                    transferencia=transferencia,
                    comentarios=comentarios,
                    ticket=ticket,
                    desglosar=desglosar
                )
                egreso.save()
                
                for product_data in products:
                    producto = Product.objects.get(id=product_data['id'])
                    total = product_data
                    product = ProductosEgreso(egreso=egreso, producto=producto, cantidad=product_data['cantidad'], entregado=True, precio=product_data['precio'], subtotal=product_data['subtotal'], iva=0, total=0)
                    product.save()
                    print(product_data['cantidad'])

            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data,safe=False)
    
    def get_context_data(self, **kwargs):
        hoy = date.today().strftime('%Y-%m-%d')

        context = super().get_context_data(**kwargs)
        context['productos_lista'] = Product.objects.all()
        context['clientes_lista'] = Client.objects.all()
        context['HOY'] = hoy;
        return context


def export_pdf_view(request, id, iva):
    print('print')

