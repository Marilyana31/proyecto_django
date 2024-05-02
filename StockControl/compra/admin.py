from django.contrib import admin

# Register your models here.

from django.contrib import admin

from compra.models import Producto, Proveedor

# Register your models here.

@admin.register(Producto)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock_actual', 'proveedor')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_display_links = ('nombre',)
    #list_per_page = 3

@admin.register(Proveedor)

class ProoveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_display_links = ('nombre',)
    #list_per_page = 3


#admin.site.register(Proveedor)
#admin.site.register(Producto)