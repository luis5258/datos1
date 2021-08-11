from typing import Callable
from django.db import models
from django.db.models import deletion
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


class registro(models.Model):
    corral = models.ForeignKey("Corral",on_delete=CASCADE, verbose_name="Selecciona el corral")
    cliente = models.ForeignKey("Cliente_corral", on_delete=CASCADE)
    producto = models.ForeignKey("Producto", on_delete=CASCADE, verbose_name="Selecciona el producto")
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=75)    
    class Meta:
        db_table = 'datos_registro'

class Cliente_corral(models.Model):
    cliente = models.CharField(max_length=75)
    
    def __str__(self):
        return self.cliente

    def save(self, *args, **kwargs):
        self.cliente = (self.cliente).upper()
        return super(Cliente_corral, self).save(*args, **kwargs)

class Corral(models.Model):
    corral =  models.CharField(max_length=75) 
    cliente  =  models.CharField(max_length=75)
    tipoStatus = models.CharField(max_length=75)
    fecha = models.DateField(max_length=40)
 

    def __str__(self):
        return self.corral

    def save(self, *args, **kwargs):
        self.corral = (self.corral).upper()
        return super(Corral, self).save(*args, **kwargs)

class status(models.Model):
    estado = models.CharField(max_length=10)
    
    def __str__(self):
        return self.estado

class surtible(models.Model):
    apto = models.CharField(max_length=10)
    
    def __str__(self):
        return self.apto

class Producto(models.Model):
    producto =  models.CharField(max_length=75)
    tipoStatus = models.ForeignKey("status", on_delete=CASCADE)
    fecha = models.DateField(auto_now=False)
    apto = models.ForeignKey("surtible", on_delete=CASCADE)

    def __str__(self):
        return self.producto
    
    def save(self, *args, **kwargs):
        self.producto = (self.producto).upper()
        return super(Producto, self).save(*args, **kwargs)

class Cliente(models.Model):

    nombre =  models.CharField(max_length=75)
    direccion = models.CharField(max_length=75)
    ciudad = models.CharField(max_length=75)
    rfc = models.CharField(max_length=75)
    email = models.EmailField(max_length=75)
    contacto = models.CharField(max_length=75)
    numero = models.BigIntegerField()

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):

        self.nombre = (self.nombre).upper()
        self.direccion = (self.direccion).upper()
        self.ciudad = (self.ciudad).upper()
        self.rfc = (self.rfc).upper()
        self.contacto = (self.contacto).upper()
        return super(Cliente, self).save(*args, **kwargs)

class Provedor(models.Model):

    nombre =  models.CharField(max_length=75)
    direccion = models.CharField(max_length=75)
    ciudad = models.CharField(max_length=75)
    rfc = models.CharField(max_length=75)
    email = models.EmailField(max_length=75)
    contacto = models.CharField(max_length=75)
    numero = models.BigIntegerField()

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):

        self.nombre = (self.nombre).upper()
        self.direccion = (self.direccion).upper()
        self.ciudad = (self.ciudad).upper()
        self.rfc = (self.rfc).upper()
        self.contacto = (self.contacto).upper()
        return super(Provedor, self).save(*args, **kwargs)

class Operador(models.Model):
    nombre  =  models.CharField(max_length=75)
    estado = models.ForeignKey("status", on_delete=CASCADE)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(Operador, self).save(*args, **kwargs)


class Tipo_animal(models.Model):
    descripcion  =  models.CharField(max_length=75)
    estado = models.ForeignKey("status", on_delete=CASCADE)

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        self.descripcion = (self.descripcion).upper()
        return super(Tipo_animal, self).save(*args, **kwargs)

class Contenedores_Mat_prima(models.Model):
    clave  =  models.CharField(max_length=75, verbose_name="CLAVE")
    cliente = models.ForeignKey("Cliente", on_delete=CASCADE, verbose_name="CLIENTE")
    capacidad =  models.BigIntegerField(verbose_name="CAPACIDAD")
    estado = models.ForeignKey("status", on_delete=CASCADE, verbose_name="ESTADO")

    def __str__(self):
        return self.clave

    def save(self, *args, **kwargs):
        self.clave = (self.clave).upper()
        return super(Contenedores_Mat_prima, self).save(*args, **kwargs)

class Contenedores_Producto(models.Model):
    claves  =  models.CharField(max_length=75, verbose_name="CLAVE")
    provedor = models.ForeignKey("Provedor", on_delete=CASCADE, verbose_name="PROVEDOR")
    capacidad =  models.BigIntegerField(verbose_name="CAPACIDAD")
    estado = models.ForeignKey("status", on_delete=CASCADE, verbose_name="ESTADO")

    def __str__(self):
        return self.claves

    def save(self, *args, **kwargs):
        self.claves = (self.claves).upper()
        return super(Contenedores_Producto, self).save(*args, **kwargs)

class Unidad(models.Model):
    unidad  =  models.CharField(max_length=75)

    def __str__(self):
        return self.unidad

    def save(self, *args, **kwargs):
        self.unidad = (self.unidad).upper()
        return super(Unidad, self).save(*args, **kwargs)

class Materia_prima(models.Model):
    descripcion  =  models.CharField(max_length=75)
    precio_unitario  =  models.BigIntegerField()
    unidad =models.ForeignKey("Unidad", on_delete=CASCADE)
    estado = models.ForeignKey("status", on_delete=CASCADE)

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        self.descripcion = (self.descripcion).upper()
        return super(Materia_prima, self).save(*args, **kwargs)















