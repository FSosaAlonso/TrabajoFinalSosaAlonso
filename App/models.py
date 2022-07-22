from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Empleados(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    DNI = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.DNI}"

class Proveedores(models.Model):

    razonsocial = models.CharField(max_length=30)
    productos = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.razonsocial} - Productos: {self.productos} - Telefono: {self.telefono} - Email: {self.email}"

class Clientes(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechafactura = models.DateTimeField(auto_now_add=True)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Fecha de compra: {self.fechafactura} - Telefono: {self.telefono}"

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

