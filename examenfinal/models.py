from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=70, blank=True, unique=True)

class helado(models.Model):
    tipo = models.CharField(max_length=100)
    tam = models.CharField(max_length=100)
    sabor = models.CharField(max_length=100)
    precio = models.IntegerField(blank=True, null=True)

class factura(models.Model):
    tipohelado = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    total =models.IntegerField(blank=True, null=True)
