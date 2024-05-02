from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    dni = models.IntegerField()


    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.dni}'


class Producto(models.Model):
    nombre = models.TextField(max_length=30)
    precio = models.IntegerField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete= models.CASCADE, related_name="productos")
   
    