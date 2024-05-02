from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .helpers import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
# Create your views here.

#______________________________________________________________________________________
# Productos

@method_decorator(csrf_exempt, name='dispatch')
class ProductoListView(View):
    def get(self, request):
        productos = get_all_productos()
        data = [{'id': producto.id, 'nombre': producto.nombre, 'precio': producto.precio, 'stock_actual': producto.stock_actual, 'proveedor':producto.proveedor} for producto in productos]
        proveedores = get_all_proveedores()
        data2 = [{'id': proveedor.id, 'nombre': proveedor.nombre, 'apellido': proveedor.apellido, "dni": proveedor.dni} for proveedor in proveedores]
        contexto = {'productos': data, 'proveedores':data2}
        #print ('getRender')
        return render(request, 'productos_list.jinja', contexto)
   
    def post(self, request):
        if request.POST.get('_method') == "PUT":
            nombre = request.POST.get('nombre')
            precio = request.POST.get('precio')
            stock_actual = request.POST.get('stock_actual')
            proveedor = request.POST.get('proveedor')
            producto = Producto.objects.get(pk=request.POST.get("id"))
            producto_actualizado = update_producto(producto, nombre, precio, stock_actual, proveedor)
            HttpResponseRedirect('/productos/')
        elif request.POST.get('_method') == "DELETE":
            producto = Producto.objects.get(pk=request.POST.get("id"))
            producto_eliminado = producto.delete()
            productos = get_all_productos()
            data = [{'id': producto.id, 'nombre': producto.nombre, 'precio': producto.precio, 'stock_actual': producto.stock_actual, 'proveedor': producto.proveedor} for producto in productos]
            return render(request, 'productos_list.jinja', {'productos': data})
        else:
            
            nombre = request.POST.get('nombre')
            precio = request.POST.get('precio')
            stock_actual = request.POST.get('stock_actual')
            proveedor = request.POST.get('proveedor')
    
            producto, creado = create_producto(nombre, precio, stock_actual, proveedor)
            #print ('redirect')
            return HttpResponseRedirect('/productos/')
  

#_______________________________________________________________
#Proveedores

class ProveedoresListView(View):
    def get(self, request):
        proveedores = get_all_proveedores()
        data = [{'id': proveedor.id, 'nombre': proveedor.nombre, 'apellido': proveedor.apellido, "dni": proveedor.dni} for proveedor in proveedores]
        return render(request, 'proveedores_list.jinja', {'proveedores': data})
   
    def post(self, request):
        if request.POST.get('_method') == "PUT":
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            dni = request.POST.get('dni')
            proveedor = Proveedor.objects.get(pk=request.POST.get("id"))
            proveedor_actualizado = update_proveedor(proveedor, nombre, apellido, dni)
            HttpResponseRedirect('/proveedores/')
        elif request.POST.get('_method') == "DELETE":
            proveedor = Proveedor.objects.get(pk=request.POST.get("id"))
            proveedor_eliminado = proveedor.delete()
            proveedores = get_all_proveedores()
            data = [{'id': proveedor.id, 'nombre': proveedor.nombre, 'apellido': proveedor.apellido, "dni": proveedor.dni} for proveedor in proveedores]
            return render(request, 'proveedores_list.jinja', {'proveedores': data})
        else:
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            dni = request.POST.get('dni')
            proveedor, creado = create_proveedor(nombre, apellido, dni)
            return HttpResponseRedirect('/proveedores/')

  
