from .models import Producto,Proveedor

#___________________________________________________________________________________________________________
#Esta primera parte es para Productos

def get_all_productos():
    return Producto.objects.all()  

def get_producto_by_id(pk):  
    return Producto.objects.get(pk=pk)

def create_producto(nombre, precio, stock_actual, proveedor):
    proveedor2 = Proveedor.objects.get(pk=proveedor)
    return Producto.objects.get_or_create(nombre=nombre, precio=precio, stock_actual=stock_actual, proveedor=proveedor2) 

def update_producto(producto, nombre, precio, stock_actual, proveedor):
    producto.nombre = nombre
    producto.precio = precio
    producto.stock_actual = stock_actual
    producto.proveedor = Proveedor.objects.get(proveedor)
    producto.save(update_fields=["nombre", "precio", "stock_actual", "proveedor"])
    return producto

def delete_producto(producto):
    producto.delete()
    return True
#___________________________________________________________________________________________________________
#Esta parte es para Proveedores

def get_all_proveedores():
    return Proveedor.objects.all()  

def get_proveedor_by_id(pk):  
    return Proveedor.objects.get(pk=pk)

def create_proveedor(nombre, apellido, dni):
    return Proveedor.objects.get_or_create(nombre=nombre, apellido=apellido, dni=dni) 

def update_proveedor(proveedor, nombre, apellido, dni):
    proveedor.nombre = nombre
    proveedor.apellido = apellido
    proveedor.dni = dni
    proveedor.save(update_fields=["nombre", "apellido", "dni"])
    return proveedor

def delete_proveedor(proveedor):
    proveedor.delete()
    return True